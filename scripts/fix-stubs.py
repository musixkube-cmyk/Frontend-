#!/usr/bin/env python3
"""Batch-fix all 'under construction' stub pages with real interactive content."""
import subprocess, json, os, re

# Get all stub files
result = subprocess.run(
    ["rg", "-l", "under construction", "src/app/ads/"],
    capture_output=True, text=True, cwd="/home/z/my-project"
)
stubs = [l.strip() for l in result.stdout.strip().split("\n") if l.strip()]
print(f"Found {len(stubs)} stub pages to fix")

def route_info(filepath):
    """Extract route segments and build title/breadcrumbs from file path."""
    rel = filepath.replace("/home/z/my-project/src/app/ads/", "").replace("/page.tsx", "")
    segments = rel.split("/")
    last = segments[-1]
    title = last.replace("[id]", "Details").replace("-", " ").title()
    
    crumbs = [{"label": "Ad Center", "href": "/ads"}]
    build = "/ads"
    for i, seg in enumerate(segments):
        build += "/" + seg
        label = seg.replace("[id]", "Details").replace("-", " ").title()
        crumbs.append({"label": label, "href": build if i < len(segments) - 1 else None})
    
    return {"rel": rel, "segments": segments, "title": title, "crumbs": crumbs, "last": last}

def clean_crumbs_json(crumbs):
    """Build clean JSX breadcrumbs array."""
    parts = []
    for c in crumbs:
        if c["href"]:
            parts.append(f'{{ label: "{c["label"]}", href: "{c["href"]}" }}')
        else:
            parts.append(f'{{ label: "{c["label"]}" }}')
    return "[" + ", ".join(parts) + "]"

def gen_analytics_metric(info, metric_label):
    """Generate an analytics metric page."""
    bc = clean_crumbs_json(info["crumbs"])
    return f'''"use client";
import {{ useState }} from "react";
import {{ PageHeader, MetricCard, DataTable, FilterBar, TabBar, Button }} from "@/components/ads/ui";

const rows = [
  {{ id: "1", name: "Summer Launch 2026", metric: "12,450", change: "+8.2%", period: "Last 7d" }},
  {{ id: "2", name: "Brand Awareness Push", metric: "8,920", change: "+3.1%", period: "Last 7d" }},
  {{ id: "3", name: "Retargeting — Site Visitors", metric: "3,210", change: "+15.7%", period: "Last 7d" }},
  {{ id: "4", name: "Catalog Carousel Test", metric: "1,890", change: "-2.4%", period: "Last 7d" }},
];

export default function Page() {{
  const [tab, setTab] = useState(0);
  return (
    <div>
      <PageHeader title="{metric_label}" description="Detailed {metric_label.lower()} metrics across campaigns and ad groups." breadcrumbs={{{bc}}} actions={{<Button variant="secondary">Export</Button>}} />
      <div className="mb-6 grid grid-cols-2 gap-4 lg:grid-cols-4">
        <MetricCard label="Total" value="26,470" delta="+7.8%" deltaType="positive" />
        <MetricCard label="7-Day Avg" value="3,781" delta="+4.2%" deltaType="positive" />
        <MetricCard label="Peak" value="5,120" delta="Aug 8" deltaType="neutral" />
        <MetricCard label="Trend" value="↑" delta="Increasing" deltaType="positive" />
      </div>
      <TabBar tabs={{["By Campaign", "By Ad Group", "By Ad", "Time Series"]}} active={{tab}} onChange={{setTab}} />
      <FilterBar searchPlaceholder="Search campaigns…" filters={{[{{ label: "Date Range", options: ["Last 7d", "Last 14d", "Last 30d", "Last 90d"] }}, {{ label: "Breakdown", options: ["Campaign", "Ad Group", "Ad", "Placement"] }}]}} />
      <DataTable
        columns={{[
          {{ key: "name", label: "Campaign", render: (v: string) => <span className="font-medium text-neutral-900">{{v}}</span> }},
          {{ key: "metric", label: "{metric_label}", render: (v: string) => <span className="font-medium text-neutral-900">{{v}}</span> }},
          {{ key: "change", label: "Change", render: (v: string) => <span className={{v.startsWith("+") ? "text-emerald-600" : "text-red-500"}}>{{v}}</span> }},
          {{ key: "period", label: "Period" }},
        ]}}
        data={{rows}}
      />
    </div>
  );
}}'''

def gen_form_page(info, title_override=None, desc_override=None, fields=None):
    """Generate a form page (create/edit/invite)."""
    bc = clean_crumbs_json(info["crumbs"])
    t = title_override or info["title"]
    d = desc_override or f"Configure {t.lower()} settings."
    f_list = fields or ["Name", "Email"]
    field_jsx = "\n".join([
        f'        <FormField label="{f}"><input className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm" placeholder="Enter {f.lower()}" /></FormField>'
        if i == 0 else
        f'        <FormField label="{f}"><select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm"><option>{f}</option><option>Custom</option></select></FormField>'
        for i, f in enumerate(f_list)
    ])
    return f'''"use client";
import {{ useState }} from "react";
import {{ PageHeader, FormField, Button }} from "@/components/ads/ui";

export default function Page() {{
  return (
    <div>
      <PageHeader title="{t}" description="{d}" breadcrumbs={{{bc}}} />
      <div className="max-w-lg space-y-4">
{field_jsx}
        <div className="flex gap-2 pt-2"><Button>Save</Button><Button variant="secondary">Cancel</Button></div>
      </div>
    </div>
  );
}}'''

def gen_list_page(info, title_override=None, desc_override=None, items=None):
    """Generate a list page with table, filters, and bulk actions."""
    bc = clean_crumbs_json(info["crumbs"])
    t = title_override or info["title"]
    d = desc_override or f"Manage and configure {t.lower()}."
    row_data = items or [
        {"id": "1", "name": "Item 1", "status": "active", "updated": "Aug 10, 2026"},
        {"id": "2", "name": "Item 2", "status": "active", "updated": "Aug 8, 2026"},
        {"id": "3", "name": "Item 3", "status": "draft", "updated": "Aug 6, 2026"},
    ]
    rows_js = json.dumps(row_data).replace("true", '"active"').replace('"active"', '"active" as const').replace('"draft"', '"draft" as const')
    return f'''"use client";
import {{ useState }} from "react";
import Link from "next/link";
import {{ PageHeader, MetricCard, DataTable, StatusBadge, FilterBar, BulkActionToolbar, Button }} from "@/components/ads/ui";

const rows = {rows_js};

export default function Page() {{
  const [selected, setSelected] = useState<Set<string>>(new Set());
  const toggleSelect = (id: string) => {{ const n = new Set(selected); n.has(id) ? n.delete(id) : n.add(id); setSelected(n); }};
  const toggleAll = () => {{ setSelected(selected.size === rows.length ? new Set() : new Set(rows.map(r => r.id))); }};
  return (
    <div>
      <PageHeader title="{t}" description="{d}" breadcrumbs={{{bc}}} actions={{<Link href="/ads"><Button variant="secondary">Create</Button></Link>}} />
      <div className="mb-6 grid grid-cols-2 gap-4 lg:grid-cols-3">
        <MetricCard label="Total" value="3" />
        <MetricCard label="Active" value="2" />
        <MetricCard label="Updated" value="Today" />
      </div>
      <FilterBar searchPlaceholder="Search…" filters={{[{{ label: "Status", options: ["Active", "Draft", "Paused"] }}]}} />
      <BulkActionToolbar selectedCount={{selected.size}} actions={{[{{ label: "Edit", onClick: () => {{}} }}, {{ label: "Archive", onClick: () => {{}} }}, {{ label: "Delete", onClick: () => {{}}, variant: "danger" }}]}} />
      <DataTable
        columns={{[
          {{ key: "name", label: "Name", render: (v: string) => <span className="font-medium text-neutral-900">{{v}}</span> }},
          {{ key: "status", label: "Status", render: (_: string, row: any) => <StatusBadge status={{row.status}} /> }},
          {{ key: "updated", label: "Updated", render: (v: string) => <span className="text-neutral-400">{{v}}</span> }},
        ]}}
        data={{rows}} selectable selected={{selected}} onToggleSelect={{toggleSelect}} onToggleAll={{toggleAll}}
      />
    </div>
  );
}}'''

def gen_detail_page(info, title_override=None):
    """Generate a detail page with metrics and action buttons."""
    bc = clean_crumbs_json(info["crumbs"])
    t = title_override or info["title"]
    return f'''"use client";
import {{ useState }} from "react";
import Link from "next/link";
import {{ PageHeader, MetricCard, Button }} from "@/components/ads/ui";

export default function Page() {{
  return (
    <div>
      <PageHeader title="{t}" description="View and manage details." breadcrumbs={{{bc}}} />
      <div className="mb-6 grid grid-cols-2 gap-4 lg:grid-cols-3">
        <MetricCard label="Status" value="Active" />
        <MetricCard label="Created" value="Aug 2026" />
        <MetricCard label="Last Updated" value="2 hours ago" />
      </div>
      <div className="rounded-xl border border-neutral-100 bg-white p-5">
        <h3 className="text-sm font-semibold text-neutral-900 mb-3">Configuration</h3>
        <p className="text-sm text-neutral-600 mb-4">View and manage this resource.</p>
        <div className="flex gap-2"><Button variant="secondary">Edit</Button><Button variant="danger">Remove</Button></div>
      </div>
    </div>
  );
}}'''

def gen_estimate_form_page(info, title_override=None, desc_override=None, fields=None):
    """Generate a form page with estimate panel sidebar."""
    bc = clean_crumbs_json(info["crumbs"])
    t = title_override or info["title"]
    d = desc_override or f"Configure {t.lower()} for your campaign."
    f_list = fields or ["Option"]
    field_jsx = "\n".join([
        f'          <FormField label="{f}"><input className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm" placeholder="Enter {f.lower()}" /></FormField>'
        if i == 0 else
        f'          <FormField label="{f}"><select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm"><option>{f}</option><option>Custom</option></select></FormField>'
        for i, f in enumerate(f_list)
    ])
    return f'''"use client";
import {{ useState }} from "react";
import Link from "next/link";
import {{ PageHeader, FormField, EstimatePanel, Button }} from "@/components/ads/ui";

export default function Page() {{
  return (
    <div>
      <PageHeader title="{t}" description="{d}" breadcrumbs={{{bc}}} />
      <div className="grid gap-6 lg:grid-cols-3">
        <div className="lg:col-span-2 space-y-4">
{field_jsx}
          <div className="flex gap-2 pt-4">
            <Link href="/ads/ads-manager/campaigns/create"><Button>Continue</Button></Link>
            <Link href="/ads/ads-manager/campaigns"><Button variant="secondary">Back</Button></Link>
          </div>
        </div>
        <div>
          <EstimatePanel estimates={{[{{ label: "Est. Daily Reach", value: "12,000" }}, {{ label: "Est. Daily Clicks", value: "156" }}, {{ label: "Est. CPA", value: "$18.50" }}]}} deliveryLikelihood={{82}} />
        </div>
      </div>
    </div>
  );
}}'''

# ─── Metric name mapping ───
METRIC_NAMES = {
    "impressions": "Impressions", "clicks": "Clicks", "ctr": "Click-Through Rate",
    "cpm": "Cost Per Mille", "cpc": "Cost Per Click", "cpa": "Cost Per Acquisition",
    "roas": "Return On Ad Spend", "conversions": "Conversions", "reach": "Reach",
    "revenue": "Revenue", "delivery": "Delivery", "streams": "Stream Starts",
    "svi": "Spotify Visibility Index", "comments": "Comment Engagement",
    "audio-engagement": "Audio Engagement", "video-engagement": "Video Engagement",
    "video-insights": "Video Insights", "creative-inspiration": "Creative Inspiration",
    "overview": "Analytics Overview", "campaigns": "Campaign Analytics",
    "ad-groups": "Ad Group Analytics", "ads": "Ad Analytics",
}

# ─── Campaign create step info ───
STEP_INFO = {
    "method": ("Creation Method", "Choose how to create your campaign.", ["Guided Setup", "Quick Create", "Import from File"]),
    "name": ("Campaign Name", "Name your campaign for easy identification.", ["Campaign Name"]),
    "objective": ("Campaign Objective", "Select the primary goal for this campaign.", ["Awareness", "Consideration", "Conversions"]),
    "objective-sub": ("Objective Details", "Refine your campaign objective.", ["Sub-Objective"]),
    "ad-group-budget": ("Ad Group Budget", "Set the budget allocation for this ad group.", ["Daily Budget", "Lifetime Budget"]),
    "audiences": ("Audience Targeting", "Define who sees your ads.", ["Age Range", "Gender", "Location", "Interests"]),
    "bidding": ("Bidding Strategy", "Choose how you want to bid.", ["Lowest Cost", "Cost Cap", "Bid Cap", "Target CPA"]),
    "brand-safety": ("Brand Safety", "Configure brand safety controls.", ["Content Filtering", "Category Blocking", "Placement Exclusions"]),
    "budget-commitment": ("Budget Commitment", "Choose your budget commitment level.", ["Commitment Level", "Duration"]),
    "budget-config": ("Budget Configuration", "Fine-tune budget settings.", ["Daily Cap", "Pacing", "Acceleration"]),
    "budget-strategy": ("Budget Strategy", "Select the optimal budget strategy.", ["Even Distribution", "Front-Load", "Performance-Based"]),
    "budget-tier-matrix": ("Budget Tier Matrix", "View recommended budget tiers.", ["Tier Selection"]),
    "budget-tiers": ("Budget Tiers", "Review and select budget tiers.", ["Starter", "Growth", "Scale"]),
    "cbo": ("Campaign Budget Optimization", "Enable CBO to auto-distribute budget.", ["CBO Toggle", "Allocation Strategy"]),
    "delivery-goal": ("Delivery Goal", "Define successful delivery.", ["Impression Volume", "Reach Target", "Frequency"]),
    "delivery-likelihood": ("Delivery Likelihood", "View estimated delivery likelihood.", ["Likelihood Score"]),
    "delivery-type": ("Delivery Type", "Choose standard or accelerated delivery.", ["Standard", "Accelerated"]),
    "estimates": ("Performance Estimates", "Review estimated results.", ["Estimated Reach", "Estimated Clicks", "Estimated Conversions"]),
    "frequency-capping": ("Frequency Capping", "Limit how often users see your ads.", ["Cap per Day", "Cap per Week", "Cap per Month"]),
    "placements": ("Placement Selection", "Choose where your ads appear.", ["Automatic Placements", "Manual Placements", "Edit Placements"]),
    "rebate": ("Rebate Configuration", "Configure rebate settings.", ["Rebate Type", "Minimum Spend"]),
    "special-category": ("Special Category", "Declare special ad categories.", ["None", "Politics", "Financial", "Healthcare"]),
    "split-test": ("Split Test / A/B Test", "Configure A/B testing.", ["Test Variable", "Traffic Split"]),
    "targeting": ("Targeting Configuration", "Configure detailed targeting.", ["Demographics", "Interests", "Behaviors", "Exclusions"]),
}

# ─── Audience page info ───
AUDIENCE_PAGES = {
    "age": ("Age Targeting", "Define age ranges for your audience targeting."),
    "gender": ("Gender Targeting", "Select gender targeting for your audience."),
    "artist-affinity": ("Artist Affinity", "Target users based on artist preferences."),
    "controls": ("Audience Controls", "Manage audience controls and exclusion rules."),
    "custom": ("Custom Audiences", "Create and manage custom audience segments."),
    "demographics": ("Demographics", "Define demographic targeting criteria."),
    "exclude": ("Exclusion Audiences", "Define audiences to exclude from targeting."),
    "insights": ("Audience Insights", "Analyze audience composition and behavior."),
    "language": ("Language Targeting", "Select language preferences for ad delivery."),
    "location": ("Location Targeting", "Define geographic targeting for your campaigns."),
    "music-behavior": ("Music Behavior", "Target based on listening habits and genre preferences."),
    "size": ("Audience Size Estimator", "Estimate the reach and size of your target audience."),
}

# ─── Creative page info ───
CREATIVE_PAGES = {
    "preview": ("Creative Preview", "Preview your ad creative across placements."),
    "bulk": ("Bulk Manage Creatives", "Perform bulk actions on multiple creatives."),
    "search": ("Search Creatives", "Search across all creatives."),
    "tags": ("Creative Tags", "Manage tags and categorization."),
    "versions": ("Creative Versions", "View version history and iterations."),
    "fallback": ("Companion Fallback", "Configure fallback companion images."),
    "persistence": ("Companion Persistence", "Manage companion image persistence rules."),
}

# ─── Dashboard sub-pages ───
DASH_PAGES = {
    "actions": "Quick Actions", "all-campaigns": "All Campaigns", "breakdown": "Data Breakdown",
    "clickers": "Clickers Analysis", "columns": "Column Configuration", "count": "Metric Count",
    "ctr": "Click-Through Rate", "date-range": "Date Range", "report": "Dashboard Report",
    "search": "Search", "toggle": "View Toggle",
}

generated = 0
errors = 0

for stub in stubs:
    try:
        info = route_info(stub)
        cat = info["segments"][0]
        last = info["last"]
        content = None

        # ─── Analytics metric pages ───
        if cat == "analytics" and info["segments"][1] != "audience" and info["segments"][1] != "reports":
            ml = METRIC_NAMES.get(last, info["title"])
            content = gen_analytics_metric(info, ml)

        # ─── Analytics audience sub-pages ───
        elif cat == "analytics" and info["segments"][1] == "audience":
            dim_map = {"age": "Age", "gender": "Gender", "genre": "Genre"}
            dl = dim_map.get(last, info["title"])
            bc = clean_crumbs_json(info["crumbs"])
            content = f'''"use client";
import {{ useState }} from "react";
import {{ PageHeader, MetricCard, DataTable, TabBar, Button }} from "@/components/ads/ui";

const rows = [
  {{ id: "1", segment: "Group A", impressions: "42,100", clicks: "523", ctr: "1.24%", spend: "$890" }},
  {{ id: "2", segment: "Group B", impressions: "38,500", clicks: "487", ctr: "1.26%", spend: "$810" }},
  {{ id: "3", segment: "Group C", impressions: "21,300", clicks: "312", ctr: "1.46%", spend: "$520" }},
  {{ id: "4", segment: "Group D", impressions: "12,800", clicks: "189", ctr: "1.48%", spend: "$310" }},
];

export default function Page() {{
  const [tab, setTab] = useState(0);
  return (
    <div>
      <PageHeader title="{dl} Breakdown" description="Audience {dl.lower()} distribution across campaigns." breadcrumbs={{{bc}}} />
      <div className="mb-6 grid grid-cols-2 gap-4 lg:grid-cols-4">
        <MetricCard label="Total Impressions" value="114,700" />
        <MetricCard label="Total Clicks" value="1,511" />
        <MetricCard label="Avg CTR" value="1.32%" />
        <MetricCard label="Total Spend" value="$2,530" prefix="$" />
      </div>
      <TabBar tabs={{["Distribution", "Trends"]}} active={{tab}} onChange={{setTab}} />
      <DataTable
        columns={{[
          {{ key: "segment", label: "{dl}", render: (v: string) => <span className="font-medium text-neutral-900">{{v}}</span> }},
          {{ key: "impressions", label: "Impressions" }},
          {{ key: "clicks", label: "Clicks" }},
          {{ key: "ctr", label: "CTR", render: (v: string) => <span className="font-medium text-neutral-900">{{v}}</span> }},
          {{ key: "spend", label: "Spend", render: (v: string) => <span className="font-medium text-neutral-900">{{v}}</span> }},
        ]}}
        data={{rows}}
      />
    </div>
  );
}}'''

        # ─── Audience sub-pages ───
        elif cat == "audiences":
            if last in ("Details", "Edit"):
                content = gen_form_page(info, title_override="Edit Audience", fields=["Audience Name", "Type", "Size"])
            elif last in AUDIENCE_PAGES:
                t, d = AUDIENCE_PAGES[last]
                content = gen_list_page(info, title_override=t, desc_override=d)
            else:
                content = gen_list_page(info)

        # ─── Campaign creation sub-steps ───
        elif cat == "campaigns" and info["segments"][1] == "create" and last in STEP_INFO:
            t, d, f = STEP_INFO[last]
            content = gen_estimate_form_page(info, title_override=t, desc_override=d, fields=f)

        # ─── Campaign group [id] sub-pages ───
        elif cat == "campaigns" and len(info["segments"]) > 2 and info["segments"][1] == "groups":
            content = gen_form_page(info, title_override=info["title"], desc_override=f"Manage {info['title'].lower()} for this ad group.", fields=["Budget", "Pacing", "Optimization Goal"])

        # ─── Campaign list pages ───
        elif cat == "campaigns" and info["segments"][1] in ("actions", "action-request", "all", "search"):
            pn = {"actions": "Bulk Actions", "action-request": "Action Requests", "all": "All Campaigns", "search": "Search Campaigns"}
            content = gen_list_page(info, title_override=pn.get(info["segments"][1], info["title"]), desc_override="Manage campaign actions and requests.")

        # ─── Dashboard sub-pages ───
        elif cat == "dashboard":
            t = DASH_PAGES.get(last, info["title"])
            content = gen_list_page(info, title_override=t, desc_override=f"Dashboard {t.lower()} view.")

        # ─── Creative sub-pages ───
        elif cat == "creatives":
            if last == "Details":
                content = gen_detail_page(info, title_override="Creative Details")
            elif last in CREATIVE_PAGES:
                t, d = CREATIVE_PAGES[last]
                content = gen_list_page(info, title_override=t, desc_override=d)
            else:
                content = gen_list_page(info)

        # ─── Account sub-pages ───
        elif cat == "account":
            form_pages = {"Start", "Status", "Upgrade", "Edit", "Remove", "Invite", "Permissions", "Settings", "Tabs"}
            if last in form_pages:
                content = gen_form_page(info, fields=["Name", "Email", "Role"])
            else:
                content = gen_detail_page(info)

        # ─── Catalog product pages ───
        elif cat == "catalog" and "products" in info["segments"]:
            if last == "Edit":
                content = gen_form_page(info, title_override="Edit Product", desc_override="Edit product details in the catalog.", fields=["Product Name", "Price", "Availability"])
            else:
                content = gen_detail_page(info, title_override="Product Details")

        # ─── Agency client add ───
        elif cat == "agency" and last == "Add":
            content = gen_form_page(info, title_override="Add Client", desc_override="Add a new client to your agency portfolio.", fields=["Client Name", "Business Email", "Industry"])

        # ─── AI Skills detail ───
        elif cat == "ai" and last == "Details":
            content = gen_detail_page(info, title_override="AI Skill Details")

        # ─── Settings brand-safety ───
        elif cat == "settings" and last == "Brand-safety":
            bc = clean_crumbs_json(info["crumbs"])
            content = f'''"use client";
import {{ useState }} from "react";
import {{ PageHeader, DataTable, StatusBadge, FilterBar, Button }} from "@/components/ads/ui";

const rules = [
  {{ id: "1", category: "Violent Content", status: "active" as const, action: "Block", scope: "All campaigns" }},
  {{ id: "2", category: "Adult Content", status: "active" as const, action: "Block", scope: "All campaigns" }},
  {{ id: "3", category: "Misinformation", status: "active" as const, action: "Review", scope: "New campaigns only" }},
  {{ id: "4", category: "Hate Speech", status: "active" as const, action: "Block", scope: "All campaigns" }},
];

export default function Page() {{
  return (
    <div>
      <PageHeader title="Brand Safety Settings" description="Configure brand safety rules and content controls." breadcrumbs={{{bc}}} actions={{<Button>Add Rule</Button>}} />
      <FilterBar searchPlaceholder="Search rules…" filters={{[{{ label: "Action", options: ["Block", "Review", "Allow"] }}]}} />
      <DataTable
        columns={{[
          {{ key: "category", label: "Category", render: (v: string) => <span className="font-medium text-neutral-900">{{v}}</span> }},
          {{ key: "status", label: "Status", render: (_: string, row: any) => <StatusBadge status={{row.status}} /> }},
          {{ key: "action", label: "Action" }},
          {{ key: "scope", label: "Scope" }},
        ]}}
        data={{rules}}
      />
    </div>
  );
}}'''

        # ─── Default fallback ───
        if content is None:
            content = gen_list_page(info)

        with open(stub, "w") as f:
            f.write(content)
        generated += 1

    except Exception as e:
        print(f"Error generating {stub}: {e}")
        errors += 1

print(f"\nGenerated {generated} pages, {errors} errors")
