import asyncio, os, time
from contextlib import asynccontextmanager
import httpx
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

REGISTRY = [{
    "id": "genesis-01", "rank": "#1 GENESIS ADOPTER",
    "name": "Finance Wallet Onboarding™ (FWO™)", "region": "Global Edge • Seattle",
    "url": os.getenv("IEAAS_GENESIS_DOMAIN", "https://fwo-engine-matrix.onrender.com"),
    "stack": "IEaaS v4.1 • FAPI 2.0 • mTLS 1.3 • PostgreSQL",
    "paths": ["/", "/health", "/fwo/v1/health", "/api/v1/production/readiness", "/fwo/v1/payments/queue", "/fwo/v1/webhooks/dlq", "/fwo/v1/infrastructure/cabinets", "/telemetry/reconcile/3h"]
}]
STATE = {"platform": "Internet Equilibrium as a Service™ (IEaaS™)", "count": 1, "domains": []}

class Reg(BaseModel):
    name: str
    url: str
    region: str = "Global Edge"

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

@app.post("/api/ieaas/adopt")
async def adopt(reg: Reg):
    u = reg.url.strip().rstrip("/")
    if not u.startswith(("https://", "http://")): raise HTTPException(422, "Invalid URL")
    n = len(REGISTRY) + 1
    REGISTRY.append({"id": f"adopter-{n:02d}", "rank": f"#{n} GLOBAL ADOPTER", "name": reg.name, "region": reg.region, "url": u, "stack": "IEaaS Standard", "paths": ["/", "/health"]})
    await sweep()
    return {"status": "ADOPTED", "total": len(REGISTRY)}

@app.get("/", response_class=HTMLResponse)
async def home(): return open("index.html").read()

INQUIRIES = []

class InstallInquiry(BaseModel):
    name: str
    email: str
    domain: str
    notes: str = ""

@app.post("/api/ieaas/inquiry")
async def log_inquiry(item: InstallInquiry):
    entry = {**item.model_dump(), "received_at": round(time.time(), 2)}
    INQUIRIES.append(entry)
    return {"status": "RECEIVED", "count": len(INQUIRIES)}

@app.get("/api/ieaas/inquiries")
async def list_inquiries():
    return {"total": len(INQUIRIES), "inquiries": INQUIRIES}
