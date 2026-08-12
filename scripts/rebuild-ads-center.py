#!/usr/bin/env python3
"""
Rebuild Ad Center to match the corrected navigation model.
- 9 sidebar sections with exact items
- All routes under /ads/assets/, /ads/measure/, /ads/manage/, /ads/billing/, /ads/settings/, /ads/agency/
- 7-step campaign builder
- Every page gets real content using shared components
"""

import os

BASE = "/home/z/my-project/src/app/ads"

# ─── Shared component imports ───
CLIENT_IMPORTS = '''"use client";

import Link from "next/link";
import { useState } from "react";
import { PageHeader, MetricCard, StatusBadge, DataTable, FilterBar, BulkActionToolbar, EmptyState, Button, TabBar, FormField, EstimatePanel, PolicyPanel, ActivityTimeline, CardGrid, StatusToggle } from "@/components/ads/ui";
'''

SIMPLE_IMPORTS = '''"use client";

import Link from "next/link";
import { PageHeader, Button, TabBar, FormField, StatusToggle } from "@/components/ads/ui";
import { useState } from "react";
'''

# ─── Page templates ───

def kpi_dashboard_page(title: str, description: str, kpis: list, table_data: dict) -> str:
    """Full dashboard page with KPI cards + data table"""
    kpi_cards = []
    for kpi in kpis:
        delta_part = ""
        if kpi.get("delta"):
            dt = kpi.get("deltaType", "neutral")
            delta_part = f' delta="{kpi["delta"]}" deltaType="{dt}"'
        kpi_cards.append(f'        <MetricCard label="{kpi["label"]}" value="{kpi["value"]}"{delta_part} />')
    
    cols = table_data.get("columns", [])
    rows = table_data.get("rows", [])
    
    col_defs = []
    for col in cols:
        if col.get("render") == "status":
            col_defs.append(f'          {{ key: "{col["key"]}", label: "{col["label"]}", render: (v: string) => <StatusBadge status={{v as any}} /> }}')
        elif col.get("render") == "bold":
            col_defs.append(f'          {{ key: "{col["key"]}", label: "{col["label"]}", render: (v: string) => <span className="font-medium text-neutral-900">{{v}}</span> }}')
        elif col.get("render") == "muted":
            col_defs.append(f'          {{ key: "{col["key"]}", label: "{col["label"]}", render: (v: string) => <span className="text-neutral-400">{{v}}</span> }}')
        else:
            col_defs.append(f'          {{ key: "{col["key"]}", label: "{col["label"]}" }}')
    
    row_strs = []
    for row in rows:
        pairs = [f'{k}: "{v}"' for k, v in row.items()]
        row_strs.append(f'            {{ {", ".join(pairs)} }},')
    
    return f'''{CLIENT_IMPORTS}
export default function {safe_name(title)}Page() {{
  const [selected, setSelected] = useState<Set<string>>(new Set());
  const [search, setSearch] = useState("");
  const toggleSelect = (id: string) => {{ const n = new Set(selected); n.has(id) ? n.delete(id) : n.add(id); setSelected(n); }};
  const toggleAll = () => {{ setSelected(selected.size === {len(rows)} ? new Set() : new Set([{",".join([f'"{r["id"]}"' for r in rows])}].map(String))); }};

  return (
    <div>
      <PageHeader title="{title}" description="{description}" />

      <div className="mb-6 grid grid-cols-2 gap-4 lg:grid-cols-{len(kpis)}">
{chr(10).join(kpi_cards)}
      </div>

      <FilterBar searchPlaceholder="Search…" onSearch={{setSearch}} />

      <BulkActionToolbar selectedCount={{selected.size}} actions={{[
        {{ label: "Pause", onClick: () => {{}} }},
        {{ label: "Resume", onClick: () => {{}} }},
        {{ label: "Delete", onClick: () => {{}}, variant: "danger" as const }},
      ]}} />

      <DataTable
        columns={{[
{chr(10).join(col_defs)}
        ]}}
        data={{[
{chr(10).join(row_strs)}
        ]}}
        selectable
        selected={{selected}}
        onToggleSelect={{toggleSelect}}
        onToggleAll={{toggleAll}}
      />
    </div>
  );
}}
'''


def list_page(title: str, description: str, items_label: str, columns: list, rows: list, create_href: str = "", create_label: str = "", filters: list = None, bulk_actions: list = None) -> str:
    """Standard list page with table, filters, bulk actions"""
    col_defs = []
    for col in columns:
        if col.get("render") == "status":
            col_defs.append(f'          {{ key: "{col["key"]}", label: "{col["label"]}", render: (v: string) => <StatusBadge status={{v as any}} /> }}')
        elif col.get("render") == "bold":
            col_defs.append(f'          {{ key: "{col["key"]}", label: "{col["label"]}", render: (v: string) => <span className="font-medium text-neutral-900">{{v}}</span> }}')
        else:
            col_defs.append(f'          {{ key: "{col["key"]}", label: "{col["label"]}" }}')
    
    row_strs = []
    for row in rows:
        pairs = [f'{k}: "{v}"' for k, v in row.items()]
        row_strs.append(f'          {{ {", ".join(pairs)} }}')
    
    action_part = ""
    if create_href:
        action_part = f'actions={{<Link href="{create_href}"><Button>{create_label}</Button></Link>}}'
    
    filter_part = ""
    if filters:
        filter_items = []
        for f in filters:
            opts = ", ".join([f'"{o}"' for o in f["options"]])
            filter_items.append(f'          {{ label: "{f["label"]}", options: [{opts}] }}')
        filter_part = f'''
      <FilterBar searchPlaceholder="Search {items_label.lower()}…" onSearch={{setSearch}} filters={{[
{chr(10).join(filter_items)}
      ]}} />'''
    else:
        filter_part = f'\n      <FilterBar searchPlaceholder="Search {items_label.lower()}…" onSearch={{setSearch}} />'
    
    bulk_part = ""
    if bulk_actions:
        ba_items = []
        for ba in bulk_actions:
            v = f', variant: "{ba["variant"]}" as const' if ba.get("variant") else ""
            ba_items.append(f'          {{ label: "{ba["label"]}", onClick: () => {{}}{v} }}')
        bulk_part = f'''
      <BulkActionToolbar selectedCount={{selected.size}} actions={{[
{chr(10).join(ba_items)}
      ]}} />'''
    
    return f'''{CLIENT_IMPORTS}
const {safe_name(items_label)} = [
{chr(10).join(row_strs)}
];

export default function {safe_name(title)}Page() {{
  const [selected, setSelected] = useState<Set<string>>(new Set());
  const [search, setSearch] = useState("");
  const toggleSelect = (id: string) => {{ const n = new Set(selected); n.has(id) ? n.delete(id) : n.add(id); setSelected(n); }};
  const toggleAll = () => {{ setSelected(selected.size === {safe_name(items_label)}.length ? new Set() : new Set({safe_name(items_label)}.map((item: any) => item.id))); }};

  return (
    <div>
      <PageHeader title="{title}" description="{description}" {action_part} />
{filter_part}
{bulk_part}

      <DataTable
        columns={{[
{chr(10).join(col_defs)}
        ]}}
        data={{{safe_name(items_label)}}}
        selectable
        selected={{selected}}
        onToggleSelect={{toggleSelect}}
        onToggleAll={{toggleAll}}
      />
    </div>
  );
}}
'''


def tabbed_page(title: str, description: str, tabs: list) -> str:
    """Page with tabs, each tab has placeholder content"""
    tab_names = [f'"{t["name"]}"' for t in tabs]
    tab_cases = []
    for i, tab in enumerate(tabs):
        content = tab.get("content", f'<div className="rounded-xl border border-neutral-100 bg-white p-6"><p className="text-sm text-neutral-500">{tab["name"]} content</p></div>')
        tab_cases.append(f'''      {{tab === {i} && (
        {content}
      )}}''')
    
    return f'''{CLIENT_IMPORTS}
export default function {safe_name(title)}Page() {{
  const [tab, setTab] = useState(0);

  return (
    <div>
      <PageHeader title="{title}" description="{description}" />
      <TabBar tabs={{[{", ".join(tab_names)}]}} active={{tab}} onChange={{setTab}} />
{chr(10).join(tab_cases)}
    </div>
  );
}}
'''


def form_page(title: str, description: str, fields: list, save_label: str = "Save") -> str:
    """Settings-style form page"""
    field_strs = []
    for f in fields:
        desc_part = f'\n          description="{f["description"]}"' if f.get("description") else ""
        if f.get("type") == "select":
            opts = f.get("options", [])
            opt_strs = [f'<option key="{{o}}">{{o}}</option>' for o in opts]
            field_strs.append(f'''        <FormField label="{f["label"]}"{desc_part}>
          <select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-700 focus:border-neutral-400 focus:outline-none">
            {[f"<option>{o}</option>" for o in opts]}
          </select>
        </FormField>''')
        elif f.get("type") == "textarea":
            field_strs.append(f'''        <FormField label="{f["label"]}"{desc_part}>
          <textarea className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-700 focus:border-neutral-400 focus:outline-none" rows={{3}} />
        </FormField>''')
        elif f.get("type") == "toggle":
            field_strs.append(f'''        <FormField label="{f["label"]}"{desc_part}>
          <StatusToggle active={{false}} onToggle={{() => {{}}}} />
        </FormField>''')
        else:
            field_strs.append(f'''        <FormField label="{f["label"]}"{desc_part}>
          <input type="text" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-700 focus:border-neutral-400 focus:outline-none" />
        </FormField>''')
    
    return f'''{SIMPLE_IMPORTS}
export default function {safe_name(title)}Page() {{
  return (
    <div>
      <PageHeader title="{title}" description="{description}" />
      <div className="max-w-2xl space-y-5">
{chr(10).join(field_strs)}
        <div className="pt-4">
          <Button>{save_label}</Button>
        </div>
      </div>
    </div>
  );
}}
'''


def simple_page(title: str, description: str) -> str:
    """Simple page with just header and description"""
    return f'''{SIMPLE_IMPORTS}
export default function {safe_name(title)}Page() {{
  return (
    <div>
      <PageHeader title="{title}" description="{description}" />
      <div className="rounded-xl border border-neutral-100 bg-white p-6">
        <p className="text-sm text-neutral-500">Content for {title} will appear here.</p>
      </div>
    </div>
  );
}}
'''


def card_grid_page(title: str, description: str, cards: list) -> str:
    """Page with a card grid of action items"""
    card_strs = []
    for c in cards:
        desc_part = f', description: "{c["description"]}"' if c.get("description") else ""
        card_strs.append(f'        {{ label: "{c["label"]}", href: "{c["href"]}"{desc_part} }}')
    
    return f'''{CLIENT_IMPORTS}
export default function {safe_name(title)}Page() {{
  return (
    <div>
      <PageHeader title="{title}" description="{description}" />
      <CardGrid cards={{[
{chr(10).join(card_strs)}
      ]}} />
    </div>
  );
}}
'''


def safe_name(s: str) -> str:
    """Convert title to valid JS identifier"""
    return s.replace("&", "And").replace("/", "").replace(" ", "").replace("-", "").replace(",", "").replace("(", "").replace(")", "").replace(".", "")


def write_page(path: str, content: str):
    """Write page content to file, creating directories as needed.
    Also fixes missing commas in JSX arrays: } followed by newline + { needs a comma."""
    import re
    # Fix: } \n { → }, \n {
    content = re.sub(r'\}\n(\s+)\{', r'},\n\1{', content)
    # Fix: ]} → , in columns/data arrays  — specifically } \n ] patterns don't need comma, but } \n { does
    # Also fix JSX prop arrays: }} followed by newline and another {{ (double braces in f-strings)
    
    full_path = os.path.join(BASE, path, "page.tsx")
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w") as f:
        f.write(content)
    return full_path


# ═══════════════════════════════════════════════════════
# GENERATE ALL PAGES
# ═══════════════════════════════════════════════════════

generated = []

# ─── OVERVIEW ───
# Dashboard already exists at /ads/page.tsx — skip
# All Campaigns already exists at /ads/campaigns/page.tsx — skip

# GMV Max
write_page("gmv-max", kpi_dashboard_page(
    "GMV Max", "Maximize gross merchandise value with optimized campaign delivery.",
    [
        {"label": "GMV", "value": "$124K", "delta": "+18%", "deltaType": "positive"},
        {"label": "ROAS", "value": "4.2x", "delta": "+0.3x", "deltaType": "positive"},
        {"label": "Active campaigns", "value": "8"},
        {"label": "Avg. order value", "value": "$31.20", "delta": "+$2.40", "deltaType": "positive"},
    ],
    {
        "columns": [
            {"key": "name", "label": "Campaign", "render": "bold"},
            {"key": "status", "label": "Status", "render": "status"},
            {"key": "gmv", "label": "GMV"},
            {"key": "roas", "label": "ROAS"},
            {"key": "spend", "label": "Spend"},
        ],
        "rows": [
            {"id": "1", "name": "GMV Max — Electronics", "status": "active", "gmv": "$52K", "roas": "5.1x", "spend": "$10.2K"},
            {"id": "2", "name": "GMV Max — Apparel", "status": "active", "gmv": "$38K", "roas": "3.8x", "spend": "$10K"},
            {"id": "3", "name": "GMV Max — Music Gear", "status": "paused", "gmv": "$34K", "roas": "3.9x", "spend": "$8.7K"},
        ],
    }
))
generated.append("gmv-max")

# Notification Center
write_page("notifications", list_page(
    "Notification Center", "View and manage all account notifications and alerts.", "notifications",
    [
        {"key": "title", "label": "Notification", "render": "bold"},
        {"key": "type", "label": "Type"},
        {"key": "status", "label": "Status", "render": "status"},
        {"key": "date", "label": "Date", "render": "muted"},
    ],
    [
        {"id": "1", "title": "Campaign budget depleted", "type": "Issue", "status": "active", "date": "Aug 12, 2026"},
        {"id": "2", "title": "New feature: AI Creative Studio", "type": "Feature", "status": "draft", "date": "Aug 11, 2026"},
        {"id": "3", "title": "Invoice INV-2026-08 ready", "type": "Announcement", "status": "completed", "date": "Aug 10, 2026"},
        {"id": "4", "title": "Policy violation on Ad #4321", "type": "Issue", "status": "rejected", "date": "Aug 9, 2026"},
    ],
    filters=[{"label": "Type", "options": ["Issue", "Announcement", "Feature", "Ticket", "Promotion"]}],
    bulk_actions=[{"label": "Mark read"}, {"label": "Dismiss", "variant": "danger"}]
))
generated.append("notifications")


# ─── CAMPAIGNS ───
# campaigns/page.tsx already exists — skip
# campaigns/groups
write_page("campaigns/groups", list_page(
    "Ad Groups", "Manage ad groups across all campaigns.", "adgroups",
    [
        {"key": "name", "label": "Ad Group", "render": "bold"},
        {"key": "campaign", "label": "Campaign"},
        {"key": "status", "label": "Status", "render": "status"},
        {"key": "budget", "label": "Budget"},
        {"key": "results", "label": "Results"},
    ],
    [
        {"id": "1", "name": "AG — Summer Launch", "campaign": "Summer Launch 2026", "status": "active", "budget": "$50/day", "results": "620 clicks"},
        {"id": "2", "name": "AG — Brand Push", "campaign": "Brand Awareness Push", "status": "active", "budget": "$30/day", "results": "22K impr."},
        {"id": "3", "name": "AG — Catalog Test", "campaign": "Catalog Carousel Test", "status": "paused", "budget": "$20/day", "results": "45 clicks"},
    ],
    create_href="/ads/campaigns/create", create_label="Create Ad Group",
    filters=[{"label": "Status", "options": ["Active", "Paused", "Draft"]}, {"label": "Campaign", "options": ["Summer Launch 2026", "Brand Awareness Push"]}],
    bulk_actions=[{"label": "Pause"}, {"label": "Resume"}, {"label": "Delete", "variant": "danger"}]
))
generated.append("campaigns/groups")

# campaigns/groups/[id]
write_page("campaigns/groups/[id]", tabbed_page(
    "Ad Group Detail", "View and manage this ad group.",
    [
        {"name": "Overview", "content": '''<div className="space-y-4">
          <div className="grid grid-cols-2 gap-4 lg:grid-cols-4">
            <MetricCard label="Budget" value="$50/day" />
            <MetricCard label="Spend" value="$1,240" />
            <MetricCard label="Results" value="620 clicks" />
            <MetricCard label="CTR" value="1.8%" delta="+0.2%" deltaType="positive" />
          </div>
        </div>'''},
        {"name": "Audience"},
        {"name": "Placements"},
        {"name": "Delivery"},
        {"name": "Analytics"},
        {"name": "Activity"},
    ]
))
generated.append("campaigns/groups/[id]")

# campaigns/ads
write_page("campaigns/ads", list_page(
    "Ads", "View and manage all ads across campaigns.", "ads",
    [
        {"key": "name", "label": "Ad", "render": "bold"},
        {"key": "campaign", "label": "Campaign"},
        {"key": "status", "label": "Status", "render": "status"},
        {"key": "type", "label": "Type"},
        {"key": "results", "label": "Results"},
    ],
    [
        {"id": "1", "name": "Summer Audio Ad 1", "campaign": "Summer Launch 2026", "status": "active", "type": "Audio", "results": "340 clicks"},
        {"id": "2", "name": "Summer Companion Banner", "campaign": "Summer Launch 2026", "status": "active", "type": "Companion", "results": "280 clicks"},
        {"id": "3", "name": "Brand Push — Video", "campaign": "Brand Awareness Push", "status": "active", "type": "Video", "results": "22K impr."},
        {"id": "4", "name": "Catalog Carousel Ad", "campaign": "Catalog Carousel Test", "status": "paused", "type": "Carousel", "results": "45 clicks"},
    ],
    create_href="/ads/campaigns/create", create_label="Create Ad",
    filters=[{"label": "Status", "options": ["Active", "Paused", "Draft"]}, {"label": "Type", "options": ["Audio", "Video", "Companion", "Carousel"]}],
    bulk_actions=[{"label": "Pause"}, {"label": "Resume"}, {"label": "Duplicate"}, {"label": "Delete", "variant": "danger"}]
))
generated.append("campaigns/ads")

# campaigns/drafts
write_page("campaigns/drafts", list_page(
    "Drafts", "Resume or discard campaign drafts.", "drafts",
    [
        {"key": "name", "label": "Draft", "render": "bold"},
        {"key": "objective", "label": "Objective"},
        {"key": "status", "label": "Status", "render": "status"},
        {"key": "modified", "label": "Modified", "render": "muted"},
    ],
    [
        {"id": "1", "name": "Artist Spotlight Q3", "objective": "Consideration", "status": "draft", "modified": "Aug 10, 2026"},
        {"id": "2", "name": "Holiday Promo 2026", "objective": "Conversions", "status": "draft", "modified": "Aug 8, 2026"},
    ],
    bulk_actions=[{"label": "Resume editing"}, {"label": "Discard", "variant": "danger"}]
))
generated.append("campaigns/drafts")

# campaigns/create — 7-step builder (overwrite existing)
write_page("campaigns/create", '''"use client";

import Link from "next/link";
import { useState } from "react";
import { PageHeader, Button, FormField, EstimatePanel, PolicyPanel, StatusToggle } from "@/components/ads/ui";

const steps = ["Creation Method", "Objective", "Campaign Setup", "Plan & Commitment", "Ad Group Setup", "Ad Creation", "Review & Launch"];

const objectives = [
  { category: "Awareness", items: ["Reach"] },
  { category: "Consideration", items: ["Traffic", "Video Views", "Community Interaction", "Brand Consideration", "Music Streams"] },
  { category: "Conversion", items: ["App Promotion", "Lead Generation", "Sales"] },
];

const methods = [
  { id: "blank", label: "Blank build", desc: "Start from scratch with full control over every setting." },
  { id: "plan", label: "Plan-led build", desc: "Choose a plan first; recommended settings are pre-filled." },
  { id: "duplicate", label: "Duplicate existing campaign", desc: "Copy an existing campaign and modify as needed." },
  { id: "template", label: "Use template", desc: "Start with a proven template for your objective." },
];

export default function CreateCampaignPage() {
  const [step, setStep] = useState(0);
  const [method, setMethod] = useState("");
  const [objective, setObjective] = useState("");
  const [subObjective, setSubObjective] = useState("");

  return (
    <div>
      <PageHeader title="Create Campaign" description={`Step ${step + 1} of 7 — ${steps[step]}`} />

      {/* Step indicator */}
      <div className="mb-8 flex items-center gap-1">
        {steps.map((s, i) => (
          <div key={s} className="flex items-center gap-1">
            <div className={`flex h-8 w-8 items-center justify-center rounded-full text-xs font-semibold ${i < step ? "bg-neutral-900 text-white" : i === step ? "border-2 border-neutral-900 text-neutral-900" : "border border-neutral-200 text-neutral-400"}`}>
              {i < step ? "✓" : i + 1}
            </div>
            {i < steps.length - 1 && <div className={`h-px w-6 ${i < step ? "bg-neutral-900" : "bg-neutral-200"}`} />}
          </div>
        ))}
      </div>

      <div className="flex gap-6">
        <div className="flex-1">
          {/* Step 0: Creation Method */}
          {step === 0 && (
            <div className="space-y-4">
              <h2 className="text-lg font-semibold text-neutral-900">How do you want to create your campaign?</h2>
              <div className="grid grid-cols-2 gap-4">
                {methods.map((m) => (
                  <button
                    key={m.id}
                    onClick={() => setMethod(m.id)}
                    className={`rounded-xl border p-5 text-left transition-colors ${method === m.id ? "border-neutral-900 bg-neutral-50" : "border-neutral-200 hover:border-neutral-300"}`}
                  >
                    <h3 className="text-sm font-semibold text-neutral-900">{m.label}</h3>
                    <p className="mt-1 text-xs text-neutral-500">{m.desc}</p>
                  </button>
                ))}
              </div>
            </div>
          )}

          {/* Step 1: Objective */}
          {step === 1 && (
            <div className="space-y-6">
              {objectives.map((cat) => (
                <div key={cat.category}>
                  <h3 className="mb-3 text-sm font-semibold uppercase tracking-wider text-neutral-400">{cat.category}</h3>
                  <div className="grid grid-cols-3 gap-3">
                    {cat.items.map((item) => (
                      <button
                        key={item}
                        onClick={() => { setObjective(cat.category); setSubObjective(item); }}
                        className={`rounded-lg border px-4 py-3 text-sm font-medium transition-colors ${subObjective === item ? "border-neutral-900 bg-neutral-50 text-neutral-900" : "border-neutral-200 text-neutral-600 hover:border-neutral-300"}`}
                      >
                        {item}
                      </button>
                    ))}
                  </div>
                </div>
              ))}
            </div>
          )}

          {/* Step 2: Campaign Setup */}
          {step === 2 && (
            <div className="max-w-xl space-y-5">
              <FormField label="Campaign name">
                <input type="text" placeholder="e.g. Summer Launch 2026" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-700 focus:border-neutral-400 focus:outline-none" />
              </FormField>
              <FormField label="Special ad category" description="Required for ads about credit, employment, housing, or social issues.">
                <select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-700 focus:border-neutral-400 focus:outline-none">
                  <option>None</option>
                  <option>Credit</option>
                  <option>Employment</option>
                  <option>Housing</option>
                  <option>Social Issues</option>
                </select>
              </FormField>
              <FormField label="Split test" description="Run an A/B test on this campaign.">
                <StatusToggle active={false} onToggle={() => {}} />
              </FormField>
            </div>
          )}

          {/* Step 3: Plan & Commitment */}
          {step === 3 && (
            <div className="max-w-xl space-y-5">
              <h2 className="text-lg font-semibold text-neutral-900">Select your plan</h2>
              <div className="grid grid-cols-2 gap-4">
                {["Social Scroll — Medium", "Music Stream — Medium", "Social Scroll — Large", "Music Stream — Large"].map((plan) => (
                  <div key={plan} className="rounded-xl border border-neutral-200 p-5">
                    <h3 className="text-sm font-semibold text-neutral-900">{plan}</h3>
                    <p className="mt-1 text-xs text-neutral-500">Flat-rate plan with optimized delivery</p>
                  </div>
                ))}
              </div>
              <FormField label="Budget optimization" description="Campaign Budget Optimization (CBO) distributes budget across ad groups automatically.">
                <select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-700 focus:border-neutral-400 focus:outline-none">
                  <option>Campaign Budget Optimization (CBO)</option>
                  <option>Ad Group Budget</option>
                </select>
              </FormField>
              <FormField label="Commitment">
                <select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-700 focus:border-neutral-400 focus:outline-none">
                  <option>Daily</option>
                  <option>Weekly</option>
                  <option>Monthly</option>
                </select>
              </FormField>
              <FormField label="Budget amount">
                <input type="number" placeholder="0.00" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-700 focus:border-neutral-400 focus:outline-none" />
              </FormField>
              <FormField label="Delivery type">
                <select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-700 focus:border-neutral-400 focus:outline-none">
                  <option>Standard</option>
                  <option>Accelerated</option>
                  <option>Scheduled</option>
                </select>
              </FormField>
            </div>
          )}

          {/* Step 4: Ad Group Setup */}
          {step === 4 && (
            <div className="space-y-6">
              <FormField label="Ad group name">
                <input type="text" placeholder="e.g. AG — Summer Launch" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-700 focus:border-neutral-400 focus:outline-none" />
              </FormField>
              <div className="rounded-xl border border-neutral-100 bg-white p-5 space-y-5">
                <h3 className="text-sm font-semibold text-neutral-900">Audience</h3>
                <FormField label="Locations">
                  <input type="text" placeholder="United States, Canada…" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-700 focus:border-neutral-400 focus:outline-none" />
                </FormField>
                <FormField label="Age range">
                  <select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-700 focus:border-neutral-400 focus:outline-none">
                    <option>18–55</option><option>18–24</option><option>25–34</option><option>35–44</option><option>45–55</option><option>55+</option>
                  </select>
                </FormField>
                <FormField label="Gender">
                  <select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-700 focus:border-neutral-400 focus:outline-none">
                    <option>All</option><option>Male</option><option>Female</option><option>Non-binary</option>
                  </select>
                </FormField>
                <FormField label="Language">
                  <input type="text" placeholder="English" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-700 focus:border-neutral-400 focus:outline-none" />
                </FormField>
              </div>
              <div className="rounded-xl border border-neutral-100 bg-white p-5 space-y-5">
                <h3 className="text-sm font-semibold text-neutral-900">Placements</h3>
                <div className="grid grid-cols-2 gap-2">
                  {["Automatic (recommended)", "In-Feed Audio", "In-Feed Video", "Top Feed", "Search Ads", "Catalog Ads"].map((p) => (
                    <label key={p} className="flex items-center gap-2 text-sm text-neutral-700">
                      <input type="checkbox" className="h-4 w-4 rounded border-neutral-300" defaultChecked={p === "Automatic (recommended)"} />
                      {p}
                    </label>
                  ))}
                </div>
              </div>
              <div className="rounded-xl border border-neutral-100 bg-white p-5 space-y-5">
                <h3 className="text-sm font-semibold text-neutral-900">Delivery & Safety</h3>
                <FormField label="Frequency cap">
                  <input type="text" placeholder="e.g. 3 impressions per day" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-700 focus:border-neutral-400 focus:outline-none" />
                </FormField>
                <FormField label="Brand suitability">
                  <select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-700 focus:border-neutral-400 focus:outline-none">
                    <option>Standard</option><option>Limited</option><option>Maximal</option>
                  </select>
                </FormField>
              </div>
            </div>
          )}

          {/* Step 5: Ad Creation */}
          {step === 5 && (
            <div className="flex gap-6">
              <div className="w-64 rounded-xl border border-neutral-100 bg-white p-4">
                <h3 className="text-sm font-semibold text-neutral-900 mb-3">Asset selector</h3>
                <div className="space-y-2 text-xs text-neutral-500">
                  <div className="rounded-lg border border-neutral-200 p-2">Audio files</div>
                  <div className="rounded-lg border border-neutral-200 p-2">Companion images</div>
                  <div className="rounded-lg border border-neutral-200 p-2">Logo</div>
                  <div className="rounded-lg border border-neutral-200 p-2">From Creative Library</div>
                </div>
              </div>
              <div className="flex-1 space-y-5">
                <FormField label="Ad name">
                  <input type="text" placeholder="e.g. Summer Audio Ad 1" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-700 focus:border-neutral-400 focus:outline-none" />
                </FormField>
                <FormField label="Audio upload">
                  <div className="rounded-lg border-2 border-dashed border-neutral-200 p-8 text-center text-sm text-neutral-400">
                    Drag and drop audio file, or click to browse
                  </div>
                </FormField>
                <FormField label="Companion image">
                  <div className="rounded-lg border-2 border-dashed border-neutral-200 p-8 text-center text-sm text-neutral-400">
                    Drag and drop image, or click to browse
                  </div>
                </FormField>
                <FormField label="CTA">
                  <select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-700 focus:border-neutral-400 focus:outline-none">
                    <option>Learn More</option><option>Shop Now</option><option>Sign Up</option><option>Listen Now</option><option>Download</option>
                  </select>
                </FormField>
                <FormField label="Destination URL">
                  <input type="url" placeholder="https://" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-700 focus:border-neutral-400 focus:outline-none" />
                </FormField>
              </div>
              <div className="w-72 rounded-xl border border-neutral-100 bg-white p-4">
                <h3 className="text-sm font-semibold text-neutral-900 mb-3">Live preview</h3>
                <div className="flex h-64 items-center justify-center rounded-lg bg-neutral-50 text-xs text-neutral-400">Ad preview</div>
              </div>
            </div>
          )}

          {/* Step 6: Review & Launch */}
          {step === 6 && (
            <div className="flex gap-6">
              <div className="flex-1 space-y-4">
                <h2 className="text-lg font-semibold text-neutral-900">Review your campaign</h2>
                <div className="rounded-xl border border-neutral-100 bg-white p-5 space-y-3 text-sm">
                  <div className="flex justify-between"><span className="text-neutral-500">Objective</span><span className="font-medium text-neutral-900">{subObjective || "—"}</span></div>
                  <div className="flex justify-between"><span className="text-neutral-500">Campaign name</span><span className="font-medium text-neutral-900">—</span></div>
                  <div className="flex justify-between"><span className="text-neutral-500">Plan</span><span className="font-medium text-neutral-900">—</span></div>
                  <div className="flex justify-between"><span className="text-neutral-500">Budget</span><span className="font-medium text-neutral-900">—</span></div>
                  <div className="flex justify-between"><span className="text-neutral-500">Delivery type</span><span className="font-medium text-neutral-900">Standard</span></div>
                </div>
              </div>
              <div className="w-72 space-y-4">
                <EstimatePanel estimates={[
                  { label: "Estimated reach", value: "~45K" },
                  { label: "Estimated clicks", value: "~560" },
                  { label: "Estimated CPM", value: "$8.20" },
                ]} deliveryLikelihood={78} />
                <PolicyPanel issues={[]} />
              </div>
            </div>
          )}
        </div>

        {/* Context panel (steps 3+) */}
        {step >= 3 && step < 6 && (
          <div className="w-72 shrink-0 space-y-4">
            <EstimatePanel estimates={[
              { label: "Estimated reach", value: "~45K" },
              { label: "Estimated clicks", value: "~560" },
              { label: "Estimated CPM", value: "$8.20" },
            ]} deliveryLikelihood={78} />
          </div>
        )}
      </div>

      {/* Footer actions */}
      <div className="mt-8 flex items-center justify-between border-t border-neutral-200 pt-4">
        <button onClick={() => step > 0 && setStep(step - 1)} disabled={step === 0} className="text-sm font-medium text-neutral-500 disabled:opacity-30">
          Back
        </button>
        <div className="flex gap-3">
          <Button variant="secondary">Save Draft</Button>
          {step < 6 ? (
            <Button onClick={() => setStep(step + 1)}>Continue</Button>
          ) : (
            <Button>Publish Campaign</Button>
          )}
        </div>
      </div>
    </div>
  );
}
''')
generated.append("campaigns/create")


# ─── ASSETS (under /ads/assets/) ───
write_page("assets/creative-library", list_page(
    "Creative Library", "Store, search, tag, and version all your creative assets.", "assets",
    [
        {"key": "name", "label": "Asset", "render": "bold"},
        {"key": "type", "label": "Type"},
        {"key": "status", "label": "Status", "render": "status"},
        {"key": "tags", "label": "Tags"},
        {"key": "updated", "label": "Updated", "render": "muted"},
    ],
    [
        {"id": "1", "name": "Summer Audio 30s", "type": "Audio", "status": "active", "tags": "summer, launch", "updated": "Aug 10, 2026"},
        {"id": "2", "name": "Brand Companion 1200x628", "type": "Image", "status": "active", "tags": "brand, banner", "updated": "Aug 8, 2026"},
        {"id": "3", "name": "Holiday Promo Video", "type": "Video", "status": "draft", "tags": "holiday, q4", "updated": "Jul 30, 2026"},
    ],
    create_href="/ads/assets/creative-studio", create_label="Create Asset",
    filters=[{"label": "Type", "options": ["Audio", "Image", "Video"]}, {"label": "Status", "options": ["Active", "Draft", "Archived"]}],
    bulk_actions=[{"label": "Tag"}, {"label": "Archive"}, {"label": "Delete", "variant": "danger"}]
))
generated.append("assets/creative-library")

write_page("assets/creative-library/[id]", tabbed_page(
    "Asset Detail", "View asset details, versions, and usage.",
    [
        {"name": "Overview", "content": '''<div className="space-y-4">
          <div className="rounded-xl border border-neutral-100 bg-white p-6">
            <div className="flex h-48 items-center justify-center text-sm text-neutral-400">Asset preview</div>
          </div>
          <div className="grid grid-cols-2 gap-4">
            <MetricCard label="Used in campaigns" value="3" />
            <MetricCard label="Performance score" value="8.2/10" />
          </div>
        </div>'''},
        {"name": "Versions"},
        {"name": "Tags"},
        {"name": "Usage"},
    ]
))
generated.append("assets/creative-library/[id]")

write_page("assets/creative-studio", tabbed_page(
    "Creative Studio", "Build, preview, and manage creative assets.",
    [
        {"name": "Audio", "content": '''<div className="space-y-4">
          <div className="flex justify-end"><Button>Upload Audio</Button></div>
          <div className="rounded-xl border-2 border-dashed border-neutral-200 p-12 text-center text-sm text-neutral-400">
            Drag and drop audio files here, or click to browse
          </div>
        </div>'''},
        {"name": "Companion Images", "content": '''<div className="space-y-4">
          <div className="flex justify-end"><Button>Upload Image</Button></div>
          <div className="rounded-xl border-2 border-dashed border-neutral-200 p-12 text-center text-sm text-neutral-400">
            Drag and drop companion images here
          </div>
        </div>'''},
        {"name": "AI Tools", "content": '''<div className="space-y-4">
          <div className="grid grid-cols-2 gap-4">
            <div className="rounded-xl border border-neutral-200 p-5"><h3 className="text-sm font-semibold text-neutral-900">AI Script Generator</h3><p className="mt-1 text-xs text-neutral-500">Generate ad copy from a brief.</p></div>
            <div className="rounded-xl border border-neutral-200 p-5"><h3 className="text-sm font-semibold text-neutral-900">AI Voiceover</h3><p className="mt-1 text-xs text-neutral-500">Select a voice and generate audio.</p></div>
            <div className="rounded-xl border border-neutral-200 p-5"><h3 className="text-sm font-semibold text-neutral-900">AI Video</h3><p className="mt-1 text-xs text-neutral-500">Create short-form video from assets.</p></div>
            <div className="rounded-xl border border-neutral-200 p-5"><h3 className="text-sm font-semibold text-neutral-900">Background Music</h3><p className="mt-1 text-xs text-neutral-500">Browse and select background tracks.</p></div>
          </div>
        </div>'''},
        {"name": "Preview"},
    ]
))
generated.append("assets/creative-studio")

write_page("assets/creator-partnerships", tabbed_page(
    "Creator Partnerships", "Collaborate with creators, manage projects, and sync relationships.",
    [
        {"name": "Overview", "content": '''<div className="space-y-4">
          <CardGrid cards={[
            { label: "Get started with creators", href: "/ads/assets/creator-partnerships", description: "Browse and connect with creators." },
            { label: "Active projects", href: "/ads/assets/creator-partnerships", description: "Manage ongoing collaborations." },
            { label: "Creator relationships", href: "/ads/assets/creator-partnerships", description: "View and sync direct relationships." },
          ]} />
        </div>'''},
        {"name": "Projects"},
        {"name": "Creators"},
    ]
))
generated.append("assets/creator-partnerships")

# Audiences under /ads/assets/audiences
write_page("assets/audiences", list_page(
    "Audiences", "Create and manage reusable audiences — custom, lookalike, artist affinity, demographics.", "audiences",
    [
        {"key": "name", "label": "Audience", "render": "bold"},
        {"key": "type", "label": "Type"},
        {"key": "size", "label": "Size"},
        {"key": "status", "label": "Status", "render": "status"},
        {"key": "updated", "label": "Updated", "render": "muted"},
    ],
    [
        {"id": "1", "name": "Broad US 18-55", "type": "Demographic", "size": "~42M", "status": "active", "updated": "Aug 10, 2026"},
        {"id": "2", "name": "Custom — Past Purchasers", "type": "Custom", "size": "~12K", "status": "active", "updated": "Aug 8, 2026"},
        {"id": "3", "name": "Lookalike — Purchasers 1%", "type": "Lookalike", "size": "~2.1M", "status": "active", "updated": "Aug 5, 2026"},
        {"id": "4", "name": "Artist Affinity — EDM", "type": "Artist Affinity", "size": "~890K", "status": "active", "updated": "Aug 1, 2026"},
    ],
    create_href="/ads/assets/audiences/create", create_label="Create Audience",
    filters=[{"label": "Type", "options": ["Custom", "Lookalike", "Demographic", "Artist Affinity", "Music Behavior", "Exclusion"]}],
    bulk_actions=[{"label": "Create lookalike"}, {"label": "Export"}, {"label": "Delete", "variant": "danger"}]
))
generated.append("assets/audiences")

write_page("assets/audiences/[id]", tabbed_page(
    "Audience Detail", "View audience definition, size, usage, and activity.",
    [
        {"name": "Overview", "content": '''<div className="space-y-4">
          <div className="grid grid-cols-2 gap-4 lg:grid-cols-4">
            <MetricCard label="Estimated size" value="~42M" />
            <MetricCard label="Used in campaigns" value="3" />
            <MetricCard label="Type" value="Demographic" />
            <MetricCard label="Status" value="Active" />
          </div>
        </div>'''},
        {"name": "Definition"},
        {"name": "Usage"},
        {"name": "Insights"},
    ]
))
generated.append("assets/audiences/[id]")

write_page("assets/audiences/create", form_page(
    "Create Audience", "Define a new reusable audience for targeting.",
    [
        {"label": "Audience name", "type": "text"},
        {"label": "Type", "type": "select", "options": ["Custom", "Lookalike", "Demographic", "Artist Affinity", "Music Behavior", "Exclusion"]},
        {"label": "Locations", "type": "text", "description": "Countries or regions to include."},
        {"label": "Age range", "type": "select", "options": ["18-24", "25-34", "35-44", "45-55", "55+", "All"]},
        {"label": "Gender", "type": "select", "options": ["All", "Male", "Female", "Non-binary"]},
    ]
))
generated.append("assets/audiences/create")

# Catalogs
write_page("assets/catalogs", list_page(
    "Catalog Manager", "Manage product catalogs, feeds, and inventory.", "catalogs",
    [
        {"key": "name", "label": "Catalog", "render": "bold"},
        {"key": "products", "label": "Products"},
        {"key": "feed", "label": "Feed health"},
        {"key": "status", "label": "Status", "render": "status"},
        {"key": "updated", "label": "Updated", "render": "muted"},
    ],
    [
        {"id": "1", "name": "Main Product Catalog", "products": "1,240", "feed": "Healthy", "status": "active", "updated": "Aug 10, 2026"},
        {"id": "2", "name": "Holiday Collection", "products": "86", "feed": "2 warnings", "status": "active", "updated": "Aug 5, 2026"},
    ],
    create_href="/ads/assets/catalogs/create", create_label="Create Catalog",
    bulk_actions=[{"label": "Sync feed"}, {"label": "Delete", "variant": "danger"}]
))
generated.append("assets/catalogs")

write_page("assets/catalogs/products/[id]", tabbed_page(
    "Product Detail", "View and edit product information.",
    [
        {"name": "Overview", "content": '''<div className="space-y-4">
          <div className="grid grid-cols-2 gap-4">
            <MetricCard label="Price" value="$29.99" />
            <MetricCard label="Availability" value="In stock" />
          </div>
        </div>'''},
        {"name": "Details"},
        {"name": "Edit"},
    ]
))
generated.append("assets/catalogs/products/[id]")

write_page("assets/catalogs/formats", card_grid_page(
    "Catalog Formats", "Browse shoppable format options for your catalogs.",
    [
        {"label": "Swipeable Carousel", "href": "/ads/assets/catalogs/formats", "description": "Users swipe through product cards."},
        {"label": "Product Showcase", "href": "/ads/assets/catalogs/formats", "description": "Featured product with details."},
        {"label": "Shoppable Format", "href": "/ads/assets/catalogs/formats", "description": "Direct purchase from ad unit."},
    ]
))
generated.append("assets/catalogs/formats")

# Placements & Inventory
write_page("inventory", kpi_dashboard_page(
    "Placements & Inventory", "Review placement performance and manage inventory allocation.",
    [
        {"label": "Total impressions", "value": "142K", "delta": "+8%", "deltaType": "positive"},
        {"label": "In-Feed Audio", "value": "68K"},
        {"label": "In-Feed Video", "value": "42K"},
        {"label": "Top Feed", "value": "32K"},
    ],
    {
        "columns": [
            {"key": "placement", "label": "Placement", "render": "bold"},
            {"key": "impressions", "label": "Impressions"},
            {"key": "clicks", "label": "Clicks"},
            {"key": "ctr", "label": "CTR"},
            {"key": "status", "label": "Status", "render": "status"},
        ],
        "rows": [
            {"id": "1", "placement": "In-Feed Audio", "impressions": "68K", "clicks": "890", "ctr": "1.31%", "status": "active"},
            {"id": "2", "placement": "In-Feed Video", "impressions": "42K", "clicks": "520", "ctr": "1.24%", "status": "active"},
            {"id": "3", "placement": "Top Feed", "impressions": "32K", "clicks": "410", "ctr": "1.28%", "status": "active"},
            {"id": "4", "placement": "Search Ads", "impressions": "12K", "clicks": "180", "ctr": "1.50%", "status": "active"},
            {"id": "5", "placement": "Catalog Ads", "impressions": "8K", "clicks": "95", "ctr": "1.19%", "status": "paused"},
        ],
    }
))
generated.append("inventory")


# ─── MEASURE (under /ads/measure/) ───
write_page("measure/analytics", kpi_dashboard_page(
    "Analytics Overview", "High-level performance across all campaigns and ad groups.",
    [
        {"label": "Spend", "value": "$3,680", "delta": "+12%", "deltaType": "positive"},
        {"label": "Impressions", "value": "142K", "delta": "+8%", "deltaType": "positive"},
        {"label": "Clicks", "value": "1,760", "delta": "+5%", "deltaType": "positive"},
        {"label": "Conversions", "value": "124", "delta": "+18%", "deltaType": "positive"},
    ],
    {
        "columns": [
            {"key": "name", "label": "Campaign", "render": "bold"},
            {"key": "status", "label": "Status", "render": "status"},
            {"key": "impressions", "label": "Impressions"},
            {"key": "clicks", "label": "Clicks"},
            {"key": "ctr", "label": "CTR"},
            {"key": "cpa", "label": "CPA"},
        ],
        "rows": [
            {"id": "1", "name": "Summer Launch 2026", "status": "active", "impressions": "68K", "clicks": "890", "ctr": "1.31%", "cpa": "$2.75"},
            {"id": "2", "name": "Brand Awareness Push", "status": "active", "impressions": "42K", "clicks": "520", "ctr": "1.24%", "cpa": "$1.71"},
            {"id": "3", "name": "Catalog Carousel Test", "status": "paused", "impressions": "32K", "clicks": "350", "ctr": "1.09%", "cpa": "$3.40"},
        ],
    }
))
generated.append("measure/analytics")

write_page("measure/performance", tabbed_page(
    "Performance Metrics", "Drill into campaign, ad group, and ad-level performance.",
    [
        {"name": "Campaigns", "content": '''<div className="space-y-4">
          <div className="grid grid-cols-2 gap-4 lg:grid-cols-4">
            <MetricCard label="CPC" value="$2.09" delta="-$0.15" deltaType="positive" />
            <MetricCard label="CPM" value="$8.45" />
            <MetricCard label="CPA" value="$2.99" delta="-$0.21" deltaType="positive" />
            <MetricCard label="ROAS" value="3.4x" delta="+0.2x" deltaType="positive" />
          </div>
        </div>'''},
        {"name": "Ad Groups"},
        {"name": "Ads"},
        {"name": "Delivery"},
    ]
))
generated.append("measure/performance")

write_page("measure/audience", tabbed_page(
    "Audience Insights", "Segment visualizations and demographic breakdowns.",
    [
        {"name": "Age", "content": '''<div className="rounded-xl border border-neutral-100 bg-white p-6">
          <p className="text-sm text-neutral-500">Age distribution chart renders here.</p>
        </div>'''},
        {"name": "Gender"},
        {"name": "Genre"},
        {"name": "Location"},
    ]
))
generated.append("measure/audience")

write_page("measure/media-insights", tabbed_page(
    "Media Insights", "Video and audio scorecards, engagement charts, creative drilldowns.",
    [
        {"name": "Video Insights", "content": '''<div className="space-y-4">
          <div className="grid grid-cols-2 gap-4">
            <MetricCard label="Video views" value="24K" delta="+15%" deltaType="positive" />
            <MetricCard label="Avg. watch time" value="8.2s" />
          </div>
        </div>'''},
        {"name": "Audio Engagement"},
        {"name": "Video Engagement"},
        {"name": "Streams"},
        {"name": "SVI", "content": '''<p className="text-sm text-neutral-500 mb-4">Synchronized Visual Impressions</p>'''},
        {"name": "Creative Inspiration"},
    ]
))
generated.append("measure/media-insights")

write_page("measure/attribution", simple_page(
    "Attribution", "Conversion path analysis and attribution model comparison."
))
generated.append("measure/attribution")

write_page("measure/reports", list_page(
    "Reports", "Create, schedule, and export custom reports.", "reports",
    [
        {"key": "name", "label": "Report", "render": "bold"},
        {"key": "type", "label": "Type"},
        {"key": "schedule", "label": "Schedule"},
        {"key": "status", "label": "Status", "render": "status"},
        {"key": "lastRun", "label": "Last run", "render": "muted"},
    ],
    [
        {"id": "1", "name": "Weekly Campaign Summary", "type": "Campaign", "schedule": "Every Monday", "status": "active", "lastRun": "Aug 11, 2026"},
        {"id": "2", "name": "Monthly ROI Report", "type": "Financial", "schedule": "1st of month", "status": "active", "lastRun": "Aug 1, 2026"},
        {"id": "3", "name": "Ad Group Performance", "type": "Ad Group", "schedule": "Manual", "status": "completed", "lastRun": "Jul 28, 2026"},
    ],
    create_href="/ads/measure/reports/create", create_label="Create Report",
    bulk_actions=[{"label": "Schedule"}, {"label": "Export CSV"}, {"label": "Delete", "variant": "danger"}]
))
generated.append("measure/reports")

write_page("measure/experiments", list_page(
    "Experiments & Studies", "Manage A/B tests, lift studies, and experiments.", "experiments",
    [
        {"key": "name", "label": "Experiment", "render": "bold"},
        {"key": "type", "label": "Type"},
        {"key": "status", "label": "Status", "render": "status"},
        {"key": "startDate", "label": "Start", "render": "muted"},
    ],
    [
        {"id": "1", "name": "Summer CBO vs ABO test", "type": "Split Test", "status": "active", "startDate": "Aug 1, 2026"},
        {"id": "2", "name": "Audio vs Video lift study", "type": "Lift Study", "status": "completed", "startDate": "Jul 15, 2026"},
    ],
    create_href="/ads/measure/experiments/create", create_label="Create Experiment",
    bulk_actions=[{"label": "End"}, {"label": "Archive", "variant": "danger"}]
))
generated.append("measure/experiments")

write_page("measure/cross-media", simple_page(
    "Cross-Media Measurement", "Cross-channel measurement views for holistic performance analysis."
))
generated.append("measure/cross-media")

write_page("measure/third-party-measurement", simple_page(
    "Third-Party Measurement", "Partner list and measurement configuration for verified reporting."
))
generated.append("measure/third-party-measurement")

write_page("measure/metrics-glossary", '''"use client";

import { useState } from "react";
import { PageHeader, FormField } from "@/components/ads/ui";

const metrics = [
  { term: "CPM", definition: "Cost per thousand impressions. Calculated as (total spend / impressions) × 1,000." },
  { term: "CPC", definition: "Cost per click. Total spend divided by total clicks." },
  { term: "CPA", definition: "Cost per acquisition/action. Total spend divided by conversions." },
  { term: "CTR", definition: "Click-through rate. Clicks divided by impressions, expressed as a percentage." },
  { term: "ROAS", definition: "Return on ad spend. Revenue generated divided by ad spend." },
  { term: "GMV", definition: "Gross merchandise value. Total value of merchandise sold through ads." },
  { term: "SVI", definition: "Synchronized Visual Impressions. Impressions where audio and visual components are displayed together." },
  { term: "Reach", definition: "The number of unique users who saw your ad at least once." },
  { term: "Frequency", definition: "The average number of times each user sees your ad." },
  { term: "Viewability", definition: "Percentage of impressions that were viewable (met IAB standard)." },
  { term: "VTR", definition: "View-through rate. Video views divided by impressions." },
  { term: "Engagement Rate", definition: "Interactions (likes, comments, shares, clicks) divided by impressions." },
];

export default function MetricsGlossaryPage() {
  const [search, setSearch] = useState("");
  const filtered = search ? metrics.filter(m => m.term.toLowerCase().includes(search.toLowerCase()) || m.definition.toLowerCase().includes(search.toLowerCase())) : metrics;

  return (
    <div>
      <PageHeader title="Metrics Glossary" description="Searchable definitions for all advertising metrics." />
      <div className="mb-4">
        <FormField label="Search metrics">
          <input type="text" value={search} onChange={(e) => setSearch(e.target.value)} placeholder="e.g. CPM, ROAS…" className="w-full max-w-md rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-700 focus:border-neutral-400 focus:outline-none" />
        </FormField>
      </div>
      <div className="space-y-3">
        {filtered.map((m) => (
          <div key={m.term} className="rounded-xl border border-neutral-100 bg-white p-5">
            <h3 className="text-sm font-semibold text-neutral-900">{m.term}</h3>
            <p className="mt-1 text-sm text-neutral-500">{m.definition}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
''')
generated.append("measure/metrics-glossary")


# ─── LEADS (under /ads/leads/) ───
# leads/page.tsx already exists — skip

write_page("leads/instant-forms", list_page(
    "Instant Forms", "Create and manage lead-generation forms.", "forms",
    [
        {"key": "name", "label": "Form", "render": "bold"},
        {"key": "campaign", "label": "Campaign"},
        {"key": "submissions", "label": "Submissions"},
        {"key": "status", "label": "Status", "render": "status"},
        {"key": "created", "label": "Created", "render": "muted"},
    ],
    [
        {"id": "1", "name": "Summer Lead Form", "campaign": "Summer Launch 2026", "submissions": "48", "status": "active", "created": "Jul 15, 2026"},
        {"id": "2", "name": "Brand Interest Form", "campaign": "Brand Awareness Push", "submissions": "22", "status": "active", "created": "Aug 1, 2026"},
    ],
    create_href="/ads/leads/instant-forms/create", create_label="Create Form",
    bulk_actions=[{"label": "Preview"}, {"label": "Delete", "variant": "danger"}]
))
generated.append("leads/instant-forms")

write_page("leads/website-forms", list_page(
    "Website Forms", "Track leads from website form submissions.", "websiteleads",
    [
        {"key": "source", "label": "Source", "render": "bold"},
        {"key": "leads", "label": "Leads"},
        {"key": "campaign", "label": "Campaign"},
        {"key": "status", "label": "Status", "render": "status"},
    ],
    [
        {"id": "1", "source": "Homepage contact form", "leads": "34", "campaign": "Summer Launch 2026", "status": "active"},
        {"id": "2", "source": "Pricing page form", "leads": "18", "campaign": "Brand Awareness Push", "status": "active"},
    ]
))
generated.append("leads/website-forms")

write_page("leads/direct-messages", simple_page(
    "Direct Messages", "Conversation-to-lead workspace for managing DM leads."
))
generated.append("leads/direct-messages")

write_page("leads/inbox", simple_page(
    "Inbox", "Unified conversation inbox with response and assignment workflows."
))
generated.append("leads/inbox")

write_page("leads/messaging", form_page(
    "Messaging Settings", "Configure messaging preferences and assistant behavior.",
    [
        {"label": "Auto-reply enabled", "type": "toggle"},
        {"label": "Response time target", "type": "select", "options": ["1 hour", "4 hours", "24 hours", "48 hours"]},
        {"label": "Message assistant", "type": "toggle", "description": "AI assistant responds to common questions automatically."},
        {"label": "Business hours", "type": "text", "description": "e.g. Mon-Fri 9am-6pm EST"},
    ]
))
generated.append("leads/messaging")

# leads/crm already exists — skip


# ─── MANAGE (under /ads/manage/) ───
write_page("manage/events", kpi_dashboard_page(
    "Events Manager", "Configure conversion events and data sources.",
    [
        {"label": "Active events", "value": "12"},
        {"label": "Data sources", "value": "4"},
        {"label": "Conversions (7d)", "value": "1,240", "delta": "+22%", "deltaType": "positive"},
        {"label": "Attribution window", "value": "7 days"},
    ],
    {
        "columns": [
            {"key": "name", "label": "Event", "render": "bold"},
            {"key": "source", "label": "Source"},
            {"key": "conversions", "label": "Conversions (7d)"},
            {"key": "status", "label": "Status", "render": "status"},
        ],
        "rows": [
            {"id": "1", "name": "Purchase", "source": "Website pixel", "conversions": "680", "status": "active"},
            {"id": "2", "name": "Add to cart", "source": "App SDK", "conversions": "340", "status": "active"},
            {"id": "3", "name": "Lead", "source": "CRM", "conversions": "220", "status": "active"},
        ],
    }
))
generated.append("manage/events")

write_page("manage/rules", '''"use client";

import Link from "next/link";
import { useState } from "react";
import { PageHeader, FilterBar, DataTable, StatusBadge, BulkActionToolbar, Button, StatusToggle } from "@/components/ads/ui";

const rules = [
  { id: "1", name: "Pause low CTR campaigns", condition: "CTR < 0.5% for 3 days", action: "Pause campaign", status: "active" as const, triggers: "14" },
  { id: "2", name: "Budget increase for winners", condition: "ROAS > 4x for 7 days", action: "Increase budget 20%", status: "active" as const, triggers: "8" },
  { id: "3", name: "Notify on spend spike", condition: "Daily spend > 2× average", action: "Send notification", status: "paused" as const, triggers: "3" },
];

export default function AutomatedRulesPage() {
  const [selected, setSelected] = useState<Set<string>>(new Set());
  const toggleSelect = (id: string) => { const n = new Set(selected); n.has(id) ? n.delete(id) : n.add(id); setSelected(n); };
  const toggleAll = () => { setSelected(selected.size === rules.length ? new Set() : new Set(rules.map(r => r.id))); };

  return (
    <div>
      <PageHeader title="Automated Rules" description="Create rules that automatically optimize your campaigns." actions={<Link href="/ads/manage/rules/create"><Button>Create Rule</Button></Link>} />
      <FilterBar searchPlaceholder="Search rules…" />
      <BulkActionToolbar selectedCount={selected.size} actions={[{ label: "Pause", onClick: () => {} }, { label: "Resume", onClick: () => {} }, { label: "Delete", onClick: () => {}, variant: "danger" as const }]} />
      <DataTable
        columns={[
          { key: "name", label: "Rule", render: (v: string) => <span className="font-medium text-neutral-900">{v}</span> },
          { key: "condition", label: "Condition" },
          { key: "action", label: "Action" },
          { key: "triggers", label: "Triggers" },
          { key: "status", label: "Status", render: (v: string) => <StatusBadge status={v as any} /> },
        ]}
        data={rules}
        selectable
        selected={selected}
        onToggleSelect={toggleSelect}
        onToggleAll={toggleAll}
      />
    </div>
  );
}
''')
generated.append("manage/rules")

write_page("manage/comments", simple_page(
    "Comments Manager", "Moderate ad comments, filter by sentiment, and respond."
))
generated.append("manage/comments")

write_page("manage/brand-safety", form_page(
    "Brand Safety", "Configure safety controls, suitability policies, and exclusions.",
    [
        {"label": "Brand suitability level", "type": "select", "options": ["Standard", "Limited", "Maximal"], "description": "Controls the sensitivity of content placement."},
        {"label": "Block list", "type": "textarea", "description": "Content categories or publishers to exclude."},
        {"label": "Content sensitivity", "type": "toggle", "description": "Enable strict content sensitivity filtering."},
        {"label": "Alcohol content", "type": "toggle"},
        {"label": "Political content", "type": "toggle"},
        {"label": "Tragedy content", "type": "toggle"},
    ]
))
generated.append("manage/brand-safety")

write_page("manage/mmm", simple_page(
    "MMM Data Requests", "Submit and track Marketing Mix Modeling data requests."
))
generated.append("manage/mmm")

write_page("manage/planning", tabbed_page(
    "Planning Tools", "Keyword research, negative keywords, and campaign planning.",
    [
        {"name": "Keyword Planner"},
        {"name": "Negative Keywords"},
    ]
))
generated.append("manage/planning")

write_page("manage/integrations", card_grid_page(
    "Integrations", "Connect and manage external integrations and partner sync.",
    [
        {"label": "Partner Sync", "href": "/ads/manage/integrations", "description": "Sync data with platform partners."},
        {"label": "Publish Content", "href": "/ads/manage/integrations", "description": "Push content to external platforms."},
        {"label": "CRM Connectors", "href": "/ads/manage/integrations", "description": "HubSpot, Salesforce, Zapier."},
        {"label": "Analytics Partners", "href": "/ads/manage/integrations", "description": "Google Analytics, Mixpanel, Amplitude."},
        {"label": "Shopify", "href": "/ads/manage/integrations", "description": "Product catalog and order sync."},
        {"label": "Custom Webhooks", "href": "/ads/manage/integrations", "description": "Configure webhook endpoints."},
    ]
))
generated.append("manage/integrations")

write_page("manage/ai-skills", card_grid_page(
    "AI Skills & MCP", "Browse, install, and manage AI skills and MCP server integrations.",
    [
        {"label": "Browse Skills", "href": "/ads/manage/ai-skills", "description": "Discover available AI skills."},
        {"label": "Installed Skills", "href": "/ads/manage/ai-skills", "description": "Manage your active AI skills."},
        {"label": "MCP Servers", "href": "/ads/manage/ai-skills", "description": "Install and configure MCP servers."},
        {"label": "Task Automation", "href": "/ads/manage/ai-skills", "description": "Set up automated AI tasks."},
    ]
))
generated.append("manage/ai-skills")


# ─── BILLING (under /ads/billing/) ───
# billing/page.tsx already exists — skip

write_page("billing/plans", tabbed_page(
    "Ads Plans & Subscriptions", "Manage your flat-rate ad plans, media plans, and subscriptions.",
    [
        {"name": "Current Plan", "content": '''<div className="space-y-4">
          <div className="rounded-xl border border-neutral-100 bg-white p-6">
            <h3 className="text-sm font-semibold text-neutral-900 mb-3">Social Scroll — Medium</h3>
            <div className="grid grid-cols-3 gap-4 text-sm">
              <div><span className="text-neutral-500">Monthly commitment</span><p className="font-medium text-neutral-900">$2,400/mo</p></div>
              <div><span className="text-neutral-500">Renewal date</span><p className="font-medium text-neutral-900">Sep 1, 2026</p></div>
              <div><span className="text-neutral-500">Status</span><p className="font-medium text-emerald-600">Active</p></div>
            </div>
          </div>
          <div className="flex gap-3">
            <Button variant="secondary">Upgrade</Button>
            <Button variant="secondary">Downgrade</Button>
            <Button variant="ghost">Cancel</Button>
          </div>
        </div>'''},
        {"name": "Available Plans"},
        {"name": "History"},
    ]
))
generated.append("billing/plans")

write_page("billing/payment-preferences", form_page(
    "Payment Preferences", "Configure automatic or manual payment settings.",
    [
        {"label": "Payment method", "type": "select", "options": ["Automatic payment", "Manual payment"]},
        {"label": "Threshold", "type": "select", "options": ["$50", "$100", "$250", "$500", "$1,000"], "description": "Charge when spend reaches this threshold."},
        {"label": "Backup payment", "type": "toggle", "description": "Use backup card if primary fails."},
    ]
))
generated.append("billing/payment-preferences")

write_page("billing/payment-methods", list_page(
    "Payment Methods", "Add and manage payment methods for your account.", "methods",
    [
        {"key": "method", "label": "Method", "render": "bold"},
        {"key": "type", "label": "Type"},
        {"key": "last4", "label": "Last 4"},
        {"key": "expiry", "label": "Expiry"},
        {"key": "isDefault", "label": "Default"},
    ],
    [
        {"id": "1", "method": "Visa ending 4242", "type": "Credit card", "last4": "4242", "expiry": "12/27", "isDefault": "Yes"},
        {"id": "2", "method": "Mastercard ending 8888", "type": "Credit card", "last4": "8888", "expiry": "06/26", "isDefault": "No"},
    ],
    create_href="/ads/billing/payment-methods/add", create_label="Add Payment Method",
    bulk_actions=[{"label": "Set default"}, {"label": "Remove", "variant": "danger"}]
))
generated.append("billing/payment-methods")

write_page("billing/profile", form_page(
    "Billing Profile", "Manage your billing identity and address.",
    [
        {"label": "Business name", "type": "text"},
        {"label": "Street address", "type": "text"},
        {"label": "City", "type": "text"},
        {"label": "State / Province", "type": "text"},
        {"label": "Postal code", "type": "text"},
        {"label": "Country", "type": "select", "options": ["United States", "Canada", "United Kingdom", "Australia"]},
    ]
))
generated.append("billing/profile")

write_page("billing/invoices", list_page(
    "Invoices", "View and download billing invoices.", "invoices",
    [
        {"key": "invoice", "label": "Invoice", "render": "bold"},
        {"key": "date", "label": "Date"},
        {"key": "amount", "label": "Amount"},
        {"key": "status", "label": "Status", "render": "status"},
        {"key": "due", "label": "Due date", "render": "muted"},
    ],
    [
        {"id": "1", "invoice": "INV-2026-08", "date": "Aug 1, 2026", "amount": "$3,680.00", "status": "active", "due": "Aug 15, 2026"},
        {"id": "2", "invoice": "INV-2026-07", "date": "Jul 1, 2026", "amount": "$2,140.00", "status": "completed", "due": "Jul 15, 2026"},
        {"id": "3", "invoice": "INV-2026-06", "date": "Jun 1, 2026", "amount": "$1,890.00", "status": "completed", "due": "Jun 15, 2026"},
    ],
    bulk_actions=[{"label": "Download PDF"}, {"label": "Export CSV"}]
))
generated.append("billing/invoices")

write_page("billing/transactions", list_page(
    "Transactions", "Full transaction history for your account.", "transactions",
    [
        {"key": "txn", "label": "Transaction", "render": "bold"},
        {"key": "type", "label": "Type"},
        {"key": "amount", "label": "Amount"},
        {"key": "date", "label": "Date"},
        {"key": "status", "label": "Status", "render": "status"},
    ],
    [
        {"id": "1", "txn": "TXN-8924", "type": "Charge", "amount": "$120.00", "date": "Aug 12, 2026", "status": "active"},
        {"id": "2", "txn": "TXN-8923", "type": "Charge", "amount": "$95.00", "date": "Aug 11, 2026", "status": "active"},
        {"id": "3", "txn": "TXN-8922", "type": "Refund", "amount": "$15.00", "date": "Aug 10, 2026", "status": "completed"},
    ]
))
generated.append("billing/transactions")

write_page("billing/taxes", form_page(
    "Taxes", "Manage tax profile and view tax documents.",
    [
        {"label": "Tax ID", "type": "text", "description": "Federal tax identification number."},
        {"label": "Tax classification", "type": "select", "options": ["LLC", "Corporation", "Sole Proprietor", "Partnership", "Non-profit"]},
        {"label": "Filing status", "type": "select", "options": ["Up to date", "Pending", "Exempt"]},
    ]
))
generated.append("billing/taxes")

write_page("billing/credits", list_page(
    "Credits, Rebates & Promotions", "View ad credits, rebate offers, and promotional balances.", "credits",
    [
        {"key": "name", "label": "Credit", "render": "bold"},
        {"key": "type", "label": "Type"},
        {"key": "amount", "label": "Amount"},
        {"key": "expires", "label": "Expires"},
        {"key": "status", "label": "Status", "render": "status"},
    ],
    [
        {"id": "1", "name": "Welcome credit", "type": "Promotional", "amount": "$500.00", "expires": "Dec 31, 2026", "status": "active"},
        {"id": "2", "name": "Spend match Q3", "type": "Match", "amount": "$250.00", "expires": "Sep 30, 2026", "status": "active"},
        {"id": "3", "name": "Rebate — Q2 overperformance", "type": "Rebate", "amount": "$75.00", "expires": "No expiry", "status": "completed"},
    ]
))
generated.append("billing/credits")

write_page("billing/support", simple_page(
    "Billing Support", "Troubleshooting articles and support intake for billing issues."
))


# ─── SETTINGS (under /ads/settings/) ───
# settings/account and settings/team already exist — skip

write_page("settings/tiers", tabbed_page(
    "Plan & Tier Status", "View account tier status and upgrade requirements.",
    [
        {"name": "Current Tier", "content": '''<div className="space-y-4">
          <div className="rounded-xl border border-neutral-100 bg-white p-6">
            <div className="flex items-center justify-between">
              <div>
                <h3 className="text-sm font-semibold text-neutral-900">Tier 2 — Growth</h3>
                <p className="mt-1 text-xs text-neutral-500">Increased limits and priority support</p>
              </div>
              <span className="inline-flex items-center rounded-full bg-emerald-50 px-2.5 py-1 text-xs font-medium text-emerald-700">Active</span>
            </div>
          </div>
          <Button variant="secondary">View upgrade requirements</Button>
        </div>'''},
        {"name": "Requirements"},
        {"name": "History"},
    ]
))
generated.append("settings/tiers")

write_page("settings/verification", tabbed_page(
    "Verification", "Business verification status and eligibility.",
    [
        {"name": "Status", "content": '''<div className="space-y-3">
          <div className="rounded-xl border border-neutral-100 bg-white p-5">
            <h3 className="text-sm font-semibold text-neutral-900 mb-3">Verification status</h3>
            <div className="space-y-2 text-sm">
              <div className="flex justify-between"><span className="text-neutral-500">Business verification</span><StatusBadge status="active" /></div>
              <div className="flex justify-between"><span className="text-neutral-500">Creator-engagement eligibility</span><StatusBadge status="active" /></div>
              <div className="flex justify-between"><span className="text-neutral-500">Analytics eligibility</span><StatusBadge status="active" /></div>
              <div className="flex justify-between"><span className="text-neutral-500">Creator-payment eligibility</span><StatusBadge status="pending_review" /></div>
            </div>
          </div>
        </div>'''},
        {"name": "Documents"},
        {"name": "Start Verification"},
    ]
))
generated.append("settings/verification")

write_page("settings/customer-review", simple_page(
    "Customer Review", "Account review status and required actions."
))
generated.append("settings/customer-review")

write_page("settings/documents", list_page(
    "Documents", "Legal and compliance document library.", "documents",
    [
        {"key": "name", "label": "Document", "render": "bold"},
        {"key": "type", "label": "Type"},
        {"key": "date", "label": "Date", "render": "muted"},
    ],
    [
        {"id": "1", "name": "Business license", "type": "Legal", "date": "Aug 1, 2026"},
        {"id": "2", "name": "Tax certificate", "type": "Tax", "date": "Jul 15, 2026"},
        {"id": "3", "name": "Insurance certificate", "type": "Compliance", "date": "Jun 30, 2026"},
    ]
))
generated.append("settings/documents")

# settings/targeting-defaults already exists — skip
# settings/notifications already exists — skip
# settings/api already exists — skip

write_page("settings/policies-security", tabbed_page(
    "Policies & Security", "Advertising policies, content guidelines, privacy, and security settings.",
    [
        {"name": "Advertising Policy"},
        {"name": "Audio Content Guidelines"},
        {"name": "Privacy Practices"},
        {"name": "Security", "content": '''<div className="space-y-4">
          <div className="rounded-xl border border-neutral-100 bg-white p-5 space-y-3">
            <h3 className="text-sm font-semibold text-neutral-900">Security overview</h3>
            <div className="space-y-2 text-sm">
              <div className="flex justify-between"><span className="text-neutral-500">Two-factor authentication</span><span className="text-emerald-600 font-medium">Enabled</span></div>
              <div className="flex justify-between"><span className="text-neutral-500">Session timeout</span><span className="text-neutral-700">30 minutes</span></div>
              <div className="flex justify-between"><span className="text-neutral-500">IP allowlist</span><span className="text-neutral-700">Not configured</span></div>
            </div>
          </div>
        </div>'''},
        {"name": "Brand Safety"},
    ]
))
generated.append("settings/policies-security")


# ─── AGENCY ───
write_page("agency", kpi_dashboard_page(
    "Agency Dashboard", "Agency overview with client performance and billing summaries.",
    [
        {"label": "Active clients", "value": "12"},
        {"label": "Total spend", "value": "$48K", "delta": "+15%", "deltaType": "positive"},
        {"label": "Avg. ROAS", "value": "3.8x"},
        {"label": "Agency commission", "value": "$4,200"},
    ],
    {
        "columns": [
            {"key": "client", "label": "Client", "render": "bold"},
            {"key": "spend", "label": "Spend"},
            {"key": "roas", "label": "ROAS"},
            {"key": "campaigns", "label": "Campaigns"},
            {"key": "status", "label": "Status", "render": "status"},
        ],
        "rows": [
            {"id": "1", "client": "Acme Records", "spend": "$12K", "roas": "4.2x", "campaigns": "8", "status": "active"},
            {"id": "2", "client": "Vibe Music Group", "spend": "$9K", "roas": "3.5x", "campaigns": "5", "status": "active"},
            {"id": "3", "client": "SoundWave Inc.", "spend": "$6K", "roas": "3.9x", "campaigns": "3", "status": "active"},
        ],
    }
))
generated.append("agency")

write_page("agency/clients", list_page(
    "Clients", "Manage agency clients and their ad accounts.", "clients",
    [
        {"key": "name", "label": "Client", "render": "bold"},
        {"key": "spend", "label": "Monthly spend"},
        {"key": "campaigns", "label": "Campaigns"},
        {"key": "status", "label": "Status", "render": "status"},
    ],
    [
        {"id": "1", "name": "Acme Records", "spend": "$12K", "campaigns": "8", "status": "active"},
        {"id": "2", "name": "Vibe Music Group", "spend": "$9K", "campaigns": "5", "status": "active"},
        {"id": "3", "name": "SoundWave Inc.", "spend": "$6K", "campaigns": "3", "status": "active"},
    ],
    create_href="/ads/agency/clients/add", create_label="Add Client",
    bulk_actions=[{"label": "Archive", "variant": "danger"}]
))
generated.append("agency/clients")

write_page("agency/clients/[id]", tabbed_page(
    "Client Detail", "View client account, campaigns, and performance.",
    [
        {"name": "Overview", "content": '''<div className="grid grid-cols-2 gap-4">
          <MetricCard label="Monthly spend" value="$12K" />
          <MetricCard label="ROAS" value="4.2x" />
        </div>'''},
        {"name": "Campaigns"},
        {"name": "Billing"},
    ]
))
generated.append("agency/clients/[id]")

write_page("agency/cross-client", simple_page(
    "Cross-Client Reporting", "Compare performance across all agency clients."
))
generated.append("agency/cross-client")

write_page("agency/billing", simple_page(
    "Agency Billing", "Agency-level billing workspace with commission tracking."
))
generated.append("agency/billing")

write_page("agency/team", list_page(
    "Agency Team", "Manage agency users and roles.", "members",
    [
        {"key": "name", "label": "Member", "render": "bold"},
        {"key": "email", "label": "Email"},
        {"key": "role", "label": "Role"},
        {"key": "status", "label": "Status", "render": "status"},
    ],
    [
        {"id": "1", "name": "Jordan Lee", "email": "jordan@agency.com", "role": "Admin", "status": "active"},
        {"id": "2", "name": "Sam Park", "email": "sam@agency.com", "role": "Member", "status": "active"},
        {"id": "3", "name": "Alex Rivera", "email": "alex@agency.com", "role": "Viewer", "status": "active"},
    ],
    create_href="/ads/agency/team/invite", create_label="Invite Member",
    bulk_actions=[{"label": "Remove", "variant": "danger"}]
))
generated.append("agency/team")


# ═══════════════════════════════════════════════════════
# PRINT SUMMARY
# ═══════════════════════════════════════════════════════
print(f"\n✅ Generated {len(generated)} pages:")
for g in generated:
    print(f"  /ads/{g}")
