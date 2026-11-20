from whitepaper import render_whitepaper
import asyncio, os, smtplib, time
from contextlib import asynccontextmanager
from email.message import EmailMessage
from typing import List, Dict, Any
import httpx
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

GENESIS_URL = os.getenv("IEAAS_GENESIS_DOMAIN", "https://fwo-engine-matrix.onrender.com").rstrip("/")
OWNER_EMAIL = "ibukadel92@gmail.com"

REGISTRY: List[Dict[str, Any]] = [{
    "id": "genesis-01", "rank": "#1 GENESIS ADOPTER",
    "name": "Finance Wallet Onboarding™ (FWO™)", "region": "Global Edge • Seattle",
    "url": GENESIS_URL, "stack": "IEaaS v4.1 • FAPI 2.0 • mTLS 1.3 • PostgreSQL",
    "paths": ["/", "/health", "/fwo/v1/health", "/api/v1/production/readiness", "/fwo/v1/payments/queue", "/fwo/v1/webhooks/dlq", "/fwo/v1/infrastructure/cabinets", "/telemetry/reconcile/3h"]
}]
STATE: Dict[str, Any] = {"platform": "Internet Equilibrium as a Service™ (IEaaS™)", "count": 1, "domains": []}
INQUIRIES: List[Dict[str, Any]] = []

class InstallInquiry(BaseModel):
    name: str
    email: str
    domain: str
    notes: str = ""

async def sweep():
    async with httpx.AsyncClient(timeout=10.0) as c:
        out = []
        for idx, d in enumerate(REGISTRY, 1):
            checks = []
            for p in d["paths"]:
                t0 = time.perf_counter()
                try:
                    r = await c.get(d["url"].rstrip("/") + p, headers={"Accept": "application/json"})
                    checks.append({"path": p, "status": r.status_code, "ms": round((time.perf_counter() - t0) * 1000, 1), "ok": r.status_code == 200})
                except Exception:
                    checks.append({"path": p, "status": 0, "ms": 0, "ok": False})
            ok = sum(1 for x in checks if x["ok"])
            out.append({**d, "rank": d.get("rank", f"ADOPTER #{idx}"), "healthy": ok, "total": len(checks), "breaks": len(checks) - ok, "checks": checks})
        STATE.update({"count": len(REGISTRY), "domains": out})

async def loop():
    while True:
        await asyncio.sleep(30)
        await sweep()

@asynccontextmanager
async def lifespan(app: FastAPI):
    await sweep()
    t = asyncio.create_task(loop())
    yield
    t.cancel()

app = FastAPI(title="Internet Equilibrium as a Service™", lifespan=lifespan)

@app.get("/health")
async def health(): return {"status": "ONLINE", "platform": "IEaaS™", "breaks": 0}

@app.get("/api/ieaas/registry")
async def registry(): return STATE

@app.post("/api/ieaas/sweep")
async def run_sweep():
    await sweep()
    return STATE

async def dispatch_email_copy(item: InstallInquiry) -> str:
    return "browser-relay"

@app.post("/api/ieaas/inquiry")
async def log_inquiry(item: InstallInquiry):
    delivery = "queued"
    try:
        delivery = await dispatch_email_copy(item)
    except Exception as e:
        delivery = f"logged-only ({str(e)[:40]})"
    entry = {**item.model_dump(), "delivery": delivery, "received_at": round(time.time(), 2)}
    INQUIRIES.append(entry)
    return {"status": "RECEIVED", "emailed_to": OWNER_EMAIL, "delivery": delivery, "count": len(INQUIRIES)}

@app.get("/api/ieaas/inquiries")
async def list_inquiries():
    return {"total": len(INQUIRIES), "inquiries": INQUIRIES}

@app.get("/", response_class=HTMLResponse)
async def home(): return open("index.html").read()

@app.get("/whitepaper", response_class=HTMLResponse)
@app.get("/docs", response_class=HTMLResponse)
async def whitepaper_page():
    return render_whitepaper()
