def render_whitepaper() -> str:
    s = chr(47)
    a = chr(64)
    fwo_url = f"https:{s}{s}fwo-engine-matrix" + ".onrender.com" + s
    mail_url = f"mailto:ibukadel92{a}://gmail.com"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>IEaaS™ Technical Whitepaper &amp; Protocol Specification</title>
  <style>
    body {{ margin:0; background:#040711; color:#f8fafc; font-family:ui-sans-serif,system-ui,sans-serif; line-height:1.65; padding:32px 20px; }}
    .wrap {{ max-width:860px; margin:0 auto; }}
    .nav {{ display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #1e293b; padding-bottom:14px; margin-bottom:24px; }}
    .pill {{ display:inline-block; padding:4px 12px; border-radius:999px; font-size:11px; font-weight:800; background:rgba(56,189,248,0.12); color:#38bdf8; border:1px solid rgba(56,189,248,0.35); }}
    h1 {{ font-size:clamp(26px,4.5vw,40px); font-weight:900; margin:12px 0; }}
    h2 {{ color:#38bdf8; font-size:18px; margin:24px 0 8px; border-bottom:1px solid #1e293b; padding-bottom:6px; }}
    .card {{ background:#0b1222; border:1px solid #1e293b; border-radius:12px; padding:22px; margin-bottom:18px; }}
    table {{ width:100%; border-collapse:collapse; margin-top:10px; font-size:13px; }}
    th, td {{ padding:10px; border:1px solid #1e293b; text-align:left; }}
    th {{ background:#070c18; color:#38bdf8; }}
    code {{ background:#050914; padding:2px 6px; border-radius:4px; color:#7dd3fc; }}
  </style>
</head>
<body>
  <div class="wrap">
    <div class="nav">
      <a href="{s}" style="color:#38bdf8;font-weight:700;text-decoration:none;">← Back to IEaaS™ Home</a>
      <svg width="340" height="52" viewBox="0 0 340 52" fill="none" xmlns="http://w3.org" style="display:block;">
  <defs>
    <linearGradient id="ieWordGrad" x1="0" y1="0" x2="52" y2="52" gradientUnits="userSpaceOnUse">
      <stop offset="0%" stop-color="#38bdf8"/>
      <stop offset="100%" stop-color="#6366f1"/>
    </linearGradient>
  </defs>
  <rect x="2" y="2" width="48" height="48" rx="12" fill="#0b1222" stroke="url(#ieWordGrad)" stroke-width="2"/>
  <path d="M13 26C13 20.5 17.5 16.5 22.8 19.5L29.2 23.2C34.5 26.2 39 22.2 39 26C39 31.5 34.5 35.5 29.2 32.5L22.8 28.8C17.5 25.8 13 31.5 13 26Z" stroke="url(#ieWordGrad)" stroke-width="3.2" stroke-linecap="round"/>
  <circle cx="15" cy="26" r="2.4" fill="#38bdf8"/>
  <circle cx="37" cy="26" r="2.4" fill="#818cf8"/>
  <line x1="26" y1="10" x2="26" y2="42" stroke="#38bdf8" stroke-width="1.3" stroke-dasharray="2.5 2.5"/>
  <text x="62" y="28" fill="#f8fafc" font-family="ui-sans-serif, system-ui, -apple-system, sans-serif" font-weight="900" font-size="22" letter-spacing="0.02em">IEaaS™</text>
  <text x="62" y="43" fill="#38bdf8" font-family="ui-sans-serif, system-ui, -apple-system, sans-serif" font-weight="800" font-size="9.5" letter-spacing="0.11em">INTERNET EQUILIBRIUM AS A SERVICE™</text>
</svg>
    </div>

    <h1>Internet Equilibrium as a Service™ (IEaaS™)<br><span style="font-size:20px;color:#94a3b8;font-weight:600;">Technical Whitepaper &amp; Workload Architecture</span></h1>
    <p style="color:#cbd5e1;">Authored by <strong>Ibukun Ayobami Adeleke Alli Alee</strong> • Principal Systems Architect (Seattle, WA)</p>

    <div class="card">
      <h2>1. The Core Problem: Distributed Workload Asymmetry</h2>
      <p>Modern cloud applications fail under load because synchronous client requests (checkouts, identity handshakes, ledger reads) collide with asynchronous background events (webhooks, telemetry streams, batch reconciliations). Without formal equilibrium boundaries, retry storms cause duplicate charges, dropped webhooks create silent data loss, and thread contention degrades latency.</p>
    </div>

    <div class="card">
      <h2>2. The Four-Layer Equilibrium Architecture</h2>
      <table>
        <thead><tr><th>Equilibrium Layer</th><th>Workload Failure Solved</th><th>Enforcement Mechanism</th></tr></thead>
        <tbody>
          <tr><td><strong>L1: Sync/Async Dual Plane</strong></td><td>Thread blocking &amp; stale dashboards</td><td>Sub-100ms synchronous REST endpoints paired with non-blocking <code>text/event-stream</code> (SSE) telemetry.</td></tr>
          <tr><td><strong>L2: Atomic Idempotency</strong></td><td>Retry storms &amp; duplicate charges</td><td>PostgreSQL <code>Idempotency-Key</code> ledger locks + strict <code>HTTP 422</code> schema rejection on partial payloads.</td></tr>
          <tr><td><strong>L3: Autonomous DLQ Loop</strong></td><td>Upstream 504 timeouts &amp; webhook loss</td><td>15-second async background reconciliation worker + deterministic Dead-Letter Queue (<code>DLQ</code>) replay.</td></tr>
          <tr><td><strong>L4: Multi-Tier Compute Mesh</strong></td><td>Resource contention across workloads</td><td>Isolation across Mainframe sequential locks, Mini departmental batch queues, and Micro edge concurrency bursts.</td></tr>
        </tbody>
      </table>
    </div>

    <div class="card">
      <h2>3. Production Reference Benchmark: Genesis Adopter #1</h2>
      <p><strong>Finance Wallet Onboarding™ (FWO™)</strong> (<a href="{fwo_url}" target="_blank" style="color:#38bdf8;">Live Production Matrix</a>) validates the IEaaS™ specification in continuous production:</p>
      <ul>
        <li><strong>29 / 29 Connected Web &amp; API Nodes:</strong> Dual-mode content negotiation serving JSON to automated watchdogs and interactive controls to browsers at <code>BREAKS: 0</code>.</li>
        <li><strong>98 / 100 (Grade A+) Readiness:</strong> Backed by Render PostgreSQL durability, HMAC-SHA256 webhook verification, and 137ms 12-request concurrent edge burst performance.</li>
      </ul>
    </div>

    <div class="card" style="border-color:#2563eb;text-align:center;">
      <h2 style="border:none;margin-top:0;">Deploy IEaaS™ on Your Domain or Network</h2>
      <p style="color:#94a3b8;">Ready to eliminate workload breaks across your infrastructure?</p>
      <a href="{s}" style="display:inline-block;background:linear-gradient(90deg,#0284c7,#4f46e5);color:#fff;padding:11px 22px;border-radius:8px;font-weight:700;text-decoration:none;margin-right:10px;">Request Installation</a>
      <a href="{mail_url}" style="color:#38bdf8;font-weight:700;text-decoration:none;">Contact Architect →</a>
    </div>
  </div>
</body>
</html>"""
