/**
 * Batch-fix all "under construction" stub pages with real content.
 * Each page gets interactive components matching its context.
 */
const fs = require("fs");
const path = require("path");

const STUBS = fs
  .readFileSync("/dev/stdin", "utf-8")
  .split("\n")
  .filter((l) => l.trim())
  .map((l) => l.trim());

/* ─── Title/description from route segments ─── */
function routeInfo(filePath) {
  // Extract route from file path: src/app/ads/.../page.tsx
  const rel = filePath.replace(/.*src\/app\/ads\//, "").replace(/\/page\.tsx$/, "");
  const segments = rel.split("/");
  // Convert segments to title
  const last = segments[segments.length - 1];
  const title = last
    .replace(/\[id\]/, "Details")
    .replace(/-/g, " ")
    .replace(/\b\w/g, (c) => c.toUpperCase());
  
  // Build breadcrumbs
  const crumbs = [{ label: "Ad Center", href: "/ads" }];
  let buildPath = "/ads";
  for (let i = 0; i < segments.length; i++) {
    const seg = segments[i];
    buildPath += "/" + seg;
    const segLabel = seg
      .replace(/\[id\]/, "Details")
      .replace(/-/g, " ")
      .replace(/\b\w/g, (c) => c.toUpperCase());
    crumbs.push({ label: segLabel, href: i < segments.length - 1 ? buildPath : undefined });
  }
  return { rel, segments, title, crumbs, last };
}

/* ─── Page templates based on context ─── */
function generatePage(filePath) {
  const { rel, segments, title, crumbs, last } = routeInfo(filePath);
  const crumbsJson = JSON.stringify(crumbs);
  
  // Category-specific generators
  const category = segments[0];

  // ─── Analytics metric pages ───
  if (category === "analytics") {
    const metricNames = {
      "impressions": "Impressions", "clicks": "Clicks", "ctr": "Click-Through Rate",
      "cpm": "Cost Per Mille", "cpc": "Cost Per Click", "cpa": "Cost Per Acquisition",
      "roas": "Return On Ad Spend", "conversions": "Conversions", "reach": "Reach",
      "revenue": "Revenue", "delivery": "Delivery", "streams": "Stream Starts",
      "svi": "Spotify Visibility Index", "comments": "Comment Engagement",
      "audio-engagement": "Audio Engagement", "video-engagement": "Video Engagement",
      "video-insights": "Video Insights", "creative-inspiration": "Creative Inspiration",
      "overview": "Analytics Overview", "campaigns": "Campaign Analytics",
      "ad-groups": "Ad Group Analytics", "ads": "Ad Analytics",
    };
    const metricLabel = metricNames[last] || title;
    return `"use client";
import { useState } from "react";
import { PageHeader, MetricCard, DataTable, FilterBar, TabBar, Button } from "@/components/ads/ui";

const rows = [
  { id: "1", name: "Summer Launch 2026", metric: "12,450", change: "+8.2%", period: "Last 7d" },
  { id: "2", name: "Brand Awareness Push", metric: "8,920", change: "+3.1%", period: "Last 7d" },
  { id: "3", name: "Retargeting — Site Visitors", metric: "3,210", change: "+15.7%", period: "Last 7d" },
  { id: "4", name: "Catalog Carousel Test", metric: "1,890", change: "-2.4%", period: "Last 7d" },
];

export default function Page() {
  const [tab, setTab] = useState(0);
  return (
    <div>
      <PageHeader title="${metricLabel}" description="Detailed ${metricLabel.toLowerCase()} metrics across campaigns and ad groups." breadcrumbs={${crumbsJson}} actions={<Button variant="secondary">Export</Button>} />
      <div className="mb-6 grid grid-cols-2 gap-4 lg:grid-cols-4">
        <MetricCard label="Total" value="26,470" delta="+7.8%" deltaType="positive" />
        <MetricCard label="7-Day Avg" value="3,781" delta="+4.2%" deltaType="positive" />
        <MetricCard label="Peak" value="5,120" delta="Aug 8" deltaType="neutral" />
        <MetricCard label="Trend" value="↑" delta="Increasing" deltaType="positive" />
      </div>
      <TabBar tabs={["By Campaign", "By Ad Group", "By Ad", "Time Series"]} active={tab} onChange={setTab} />
      <FilterBar searchPlaceholder="Search campaigns…" filters={[{ label: "Date Range", options: ["Last 7d", "Last 14d", "Last 30d", "Last 90d"] }, { label: "Breakdown", options: ["Campaign", "Ad Group", "Ad", "Placement"] }]} />
      <DataTable
        columns={[
          { key: "name", label: "Campaign", render: (v: string) => <span className="font-medium text-neutral-900">{v}</span> },
          { key: "metric", label: "${metricLabel}", render: (v: string) => <span className="font-medium text-neutral-900">{v}</span> },
          { key: "change", label: "Change", render: (v: string) => <span className={v.startsWith("+") ? "text-emerald-600" : "text-red-500"}>{v}</span> },
          { key: "period", label: "Period" },
        ]}
        data={rows}
      />
    </div>
  );
}`;
  }

  // ─── Analytics audience sub-pages ───
  if (category === "analytics" && segments[1] === "audience") {
    const dims = { age: "Age", gender: "Gender", genre: "Genre" };
    const dimLabel = dims[last] || title;
    return `"use client";
import { useState } from "react";
import { PageHeader, MetricCard, DataTable, TabBar, Button } from "@/components/ads/ui";

const rows = [
  { id: "1", segment: "${last === 'age' ? '18-24' : last === 'gender' ? 'Male' : 'Pop'}", impressions: "42,100", clicks: "523", ctr: "1.24%", spend: "$890" },
  { id: "2", segment: "${last === 'age' ? '25-34' : last === 'gender' ? 'Female' : 'Rock'}", impressions: "38,500", clicks: "487", ctr: "1.26%", spend: "$810" },
  { id: "3", segment: "${last === 'age' ? '35-44' : last === 'gender' ? 'Non-binary' : 'Hip-Hop'}", impressions: "21,300", clicks: "312", ctr: "1.46%", spend: "$520" },
  { id: "4", segment: "${last === 'age' ? '45-55' : last === 'gender' ? 'Other' : 'R&B'}", impressions: "12,800", clicks: "189", ctr: "1.48%", spend: "$310" },
];

export default function Page() {
  const [tab, setTab] = useState(0);
  return (
    <div>
      <PageHeader title="${dimLabel} Breakdown" description="Audience ${dimLabel.toLowerCase()} distribution across campaigns." breadcrumbs={${crumbsJson}} />
      <div className="mb-6 grid grid-cols-2 gap-4 lg:grid-cols-4">
        <MetricCard label="Total Impressions" value="114,700" />
        <MetricCard label="Total Clicks" value="1,511" />
        <MetricCard label="Avg CTR" value="1.32%" />
        <MetricCard label="Total Spend" value="$2,530" prefix="$" />
      </div>
      <TabBar tabs={["Distribution", "Trends"]} active={tab} onChange={setTab} />
      <DataTable
        columns={[
          { key: "segment", label: "${dimLabel}", render: (v: string) => <span className="font-medium text-neutral-900">{v}</span> },
          { key: "impressions", label: "Impressions" },
          { key: "clicks", label: "Clicks" },
          { key: "ctr", label: "CTR", render: (v: string) => <span className="font-medium text-neutral-900">{v}</span> },
          { key: "spend", label: "Spend", render: (v: string) => <span className="font-medium text-neutral-900">{v}</span> },
        ]}
        data={rows}
      />
    </div>
  );
}`;
  }

  // ─── Audience sub-pages ───
  if (category === "audiences") {
    const audiencePages = {
      age: { title: "Age Targeting", desc: "Define age ranges for your audience targeting.", field: "Age Range", options: ["13-17", "18-24", "25-34", "35-44", "45-55", "55+"] },
      gender: { title: "Gender Targeting", desc: "Select gender targeting for your audience.", field: "Gender", options: ["All", "Male", "Female", "Non-binary"] },
      "artist-affinity": { title: "Artist Affinity", desc: "Target users based on artist preferences and listening behavior.", field: "Artist", options: ["Taylor Swift", "Drake", "Bad Bunny", "The Weeknd"] },
      controls: { title: "Audience Controls", desc: "Manage audience controls and exclusion rules.", field: "Control", options: ["Age restriction", "Geo exclusion", "Placement exclusion"] },
      custom: { title: "Custom Audiences", desc: "Create and manage custom audience segments.", field: "Audience", options: ["Past purchasers", "Email list", "App users"] },
      demographics: { title: "Demographics", desc: "Define demographic targeting criteria.", field: "Criteria", options: ["Age", "Gender", "Location", "Language"] },
      exclude: { title: "Exclusion Audiences", desc: "Define audiences to exclude from targeting.", field: "Exclusion", options: ["Existing customers", "Past converters", "Employees"] },
      insights: { title: "Audience Insights", desc: "Analyze audience composition and behavior.", field: "Metric", options: ["Size", "Reach", "Engagement", "Conversion"] },
      language: { title: "Language Targeting", desc: "Select language preferences for ad delivery.", field: "Language", options: ["English", "Spanish", "French", "German", "Portuguese"] },
      location: { title: "Location Targeting", desc: "Define geographic targeting for your campaigns.", field: "Location", options: ["United States", "Canada", "United Kingdom", "Australia"] },
      "music-behavior": { title: "Music Behavior", desc: "Target based on listening habits, playlist activity, and genre preferences.", field: "Behavior", options: ["Playlist creators", "Heavy streamers", "Genre switchers"] },
      size: { title: "Audience Size Estimator", desc: "Estimate the reach and size of your target audience.", field: "Estimate", options: ["Narrow", "Balanced", "Broad"] },
    };
    const info = audiencePages[last] || { title, desc: `Manage ${title.toLowerCase()} for your ad audiences.`, field: title, options: ["Option A", "Option B", "Option C"] };
    // Dynamic [id] pages
    if (last === "Details") {
      return `"use client";
import { useState } from "react";
import Link from "next/link";
import { PageHeader, MetricCard, DataTable, StatusBadge, Button } from "@/components/ads/ui";

export default function Page() {
  return (
    <div>
      <PageHeader title="Audience Details" description="View and edit this audience segment." breadcrumbs={${crumbsJson}} actions={<Link href="/ads/audiences"><Button variant="secondary">Back to Audiences</Button></Link>} />
      <div className="mb-6 grid grid-cols-2 gap-4 lg:grid-cols-4">
        <MetricCard label="Audience Size" value="2.1M" />
        <MetricCard label="Reach (30d)" value="890K" />
        <MetricCard label="Type" value="Custom" />
        <MetricCard label="Status" value="Ready" />
      </div>
      <div className="rounded-xl border border-neutral-100 bg-white p-5">
        <h3 className="text-sm font-semibold text-neutral-900 mb-3">Audience Configuration</h3>
        <div className="space-y-3 text-sm text-neutral-700">
          <p>This audience was built from custom criteria and is currently active across 3 campaigns.</p>
          <div className="flex gap-2">
            <Button variant="secondary">Edit Criteria</Button>
            <Button variant="secondary">Duplicate</Button>
            <Button variant="danger">Delete</Button>
          </div>
        </div>
      </div>
    </div>
  );
}`;
    }
    if (last === "Edit") {
      return `"use client";
import { useState } from "react";
import { PageHeader, FormField, Button } from "@/components/ads/ui";

export default function Page() {
  const [name, setName] = useState("");
  return (
    <div>
      <PageHeader title="Edit Audience" description="Modify audience targeting criteria." breadcrumbs={${crumbsJson}} />
      <div className="max-w-lg space-y-4">
        <FormField label="Audience Name"><input value={name} onChange={e => setName(e.target.value)} className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm" placeholder="e.g. US 18-34 Music Lovers" /></FormField>
        <FormField label="Targeting Type"><select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm"><option>Demographic</option><option>Custom</option><option>Lookalike</option></select></FormField>
        <div className="flex gap-2 pt-2"><Button>Save Changes</Button><Button variant="secondary">Cancel</Button></div>
      </div>
    </div>
  );
}`;
    }
    return `"use client";
import { useState } from "react";
import Link from "next/link";
import { PageHeader, MetricCard, DataTable, StatusBadge, FilterBar, Button } from "@/components/ads/ui";

const rows = [
  { id: "1", name: "${info.options[0] || 'Segment A'}", size: "1.2M", status: "ready" as const, updated: "Aug 10, 2026" },
  { id: "2", name: "${info.options[1] || 'Segment B'}", size: "890K", status: "ready" as const, updated: "Aug 8, 2026" },
  { id: "3", name: "${info.options[2] || 'Segment C'}", size: "340K", status: "building" as const, updated: "Aug 6, 2026" },
];

export default function Page() {
  return (
    <div>
      <PageHeader title="${info.title}" description="${info.desc}" breadcrumbs={${crumbsJson}} actions={<Link href="/ads/audiences/create"><Button>Create</Button></Link>} />
      <div className="mb-6 grid grid-cols-2 gap-4 lg:grid-cols-3">
        <MetricCard label="Total Segments" value="3" />
        <MetricCard label="Total Reach" value="2.4M" />
        <MetricCard label="Active" value="2" />
      </div>
      <FilterBar searchPlaceholder="Search…" filters={[{ label: "Status", options: ["Ready", "Building", "Expired"] }]} />
      <DataTable
        columns={[
          { key: "name", label: "${info.field}", render: (v: string) => <span className="font-medium text-neutral-900">{v}</span> },
          { key: "size", label: "Size", render: (v: string) => <span className="font-medium text-neutral-900">{v}</span> },
          { key: "status", label: "Status", render: (_: string, row: any) => <StatusBadge status={row.status} /> },
          { key: "updated", label: "Updated", render: (v: string) => <span className="text-neutral-400">{v}</span> },
        ]}
        data={rows}
      />
    </div>
  );
}`;
  }

  // ─── Campaign creation sub-steps ───
  if (category === "campaigns" && segments[1] === "create") {
    const stepInfo = {
      method: { title: "Creation Method", desc: "Choose how to create your campaign.", fields: ["Guided Setup", "Quick Create", "Import from File"] },
      name: { title: "Campaign Name", desc: "Name your campaign for easy identification.", fields: ["Campaign Name"] },
      objective: { title: "Campaign Objective", desc: "Select the primary goal for this campaign.", fields: ["Awareness", "Consideration", "Conversions"] },
      "objective-sub": { title: "Objective Details", desc: "Refine your campaign objective with a specific sub-objective.", fields: ["Sub-Objective"] },
      "ad-group-budget": { title: "Ad Group Budget", desc: "Set the budget allocation for this ad group.", fields: ["Daily Budget", "Lifetime Budget"] },
      audiences: { title: "Audience Targeting", desc: "Define who sees your ads.", fields: ["Age Range", "Gender", "Location", "Interests"] },
      bidding: { title: "Bidding Strategy", desc: "Choose how you want to bid for ad placements.", fields: ["Lowest Cost", "Cost Cap", "Bid Cap", "Target CPA"] },
      "brand-safety": { title: "Brand Safety", desc: "Configure brand safety controls and blocklists.", fields: ["Content Filtering", "Category Blocking", "Placement Exclusions"] },
      "budget-commitment": { title: "Budget Commitment", desc: "Choose your budget commitment level and duration.", fields: ["Commitment Level", "Duration"] },
      "budget-config": { title: "Budget Configuration", desc: "Fine-tune your campaign budget settings.", fields: ["Daily Cap", "Pacing", "Acceleration"] },
      "budget-strategy": { title: "Budget Strategy", desc: "Select the optimal budget strategy for your goals.", fields: ["Even Distribution", "Front-Load", "Performance-Based"] },
      "budget-tier-matrix": { title: "Budget Tier Matrix", desc: "View recommended budget tiers by objective.", fields: ["Tier Selection"] },
      "budget-tiers": { title: "Budget Tiers", desc: "Review and select budget tier options.", fields: ["Starter", "Growth", "Scale"] },
      cbo: { title: "Campaign Budget Optimization", desc: "Enable CBO to automatically distribute budget across ad groups.", fields: ["CBO Toggle", "Allocation Strategy"] },
      "delivery-goal": { title: "Delivery Goal", desc: "Define what successful delivery looks like.", fields: ["Impression Volume", "Reach Target", "Frequency"] },
      "delivery-likelihood": { title: "Delivery Likelihood", desc: "View estimated delivery likelihood based on current settings.", fields: ["Likelihood Score"] },
      "delivery-type": { title: "Delivery Type", desc: "Choose standard or accelerated delivery.", fields: ["Standard", "Accelerated"] },
      estimates: { title: "Performance Estimates", desc: "Review estimated results based on your configuration.", fields: ["Estimated Reach", "Estimated Clicks", "Estimated Conversions"] },
      "frequency-capping": { title: "Frequency Capping", desc: "Limit how often users see your ads.", fields: ["Cap per Day", "Cap per Week", "Cap per Month"] },
      placements: { title: "Placement Selection", desc: "Choose where your ads will appear.", fields: ["Automatic Placements", "Manual Placements", "Edit Placements"] },
      rebate: { title: "Rebate Configuration", desc: "Configure rebate and discount settings.", fields: ["Rebate Type", "Minimum Spend"] },
      "special-category": { title: "Special Category", desc: "Declare special ad categories if applicable.", fields: ["None", "Politics", "Financial", "Healthcare"] },
      "split-test": { title: "Split Test / A/B Test", desc: "Configure A/B testing for your campaign.", fields: ["Test Variable", "Traffic Split"] },
      targeting: { title: "Targeting Configuration", desc: "Configure detailed targeting for this campaign.", fields: ["Demographics", "Interests", "Behaviors", "Exclusions"] },
    };
    const info = stepInfo[last] || { title, desc: `Configure ${title.toLowerCase()} for your campaign.`, fields: ["Option A", "Option B"] };
    const fieldInputs = info.fields.map((f, i) => `        <FormField label="${f}">${i === 0 ? `<input className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm" placeholder="Enter ${f.toLowerCase()}" />` : `<select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm"><option>${f}</option><option>Custom</option></select>`}</FormField>`).join("\n");
    return `"use client";
import { useState } from "react";
import Link from "next/link";
import { PageHeader, FormField, EstimatePanel, Button } from "@/components/ads/ui";

export default function Page() {
  return (
    <div>
      <PageHeader title="${info.title}" description="${info.desc}" breadcrumbs={${crumbsJson}} />
      <div className="grid gap-6 lg:grid-cols-3">
        <div className="lg:col-span-2 space-y-4">
${fieldInputs}
          <div className="flex gap-2 pt-4">
            <Link href="/ads/ads-manager/campaigns/create"><Button>Continue</Button></Link>
            <Link href="/ads/ads-manager/campaigns"><Button variant="secondary">Back</Button></Link>
          </div>
        </div>
        <div>
          <EstimatePanel estimates={[{ label: "Est. Daily Reach", value: "12,000" }, { label: "Est. Daily Clicks", value: "156" }, { label: "Est. CPA", value: "$18.50" }]} deliveryLikelihood={82} />
        </div>
      </div>
    </div>
  );
}`;
  }

  // ─── Campaign list sub-pages ───
  if (category === "campaigns" && segments[1] === "groups" && segments[2] === "[id]") {
    const subInfo = {
      budget: { title: "Ad Group Budget", desc: "Manage budget allocation for this ad group." },
      "cross-format": { title: "Cross-Format Delivery", desc: "View delivery metrics across ad formats." },
      delivery: { title: "Ad Group Delivery", desc: "Monitor delivery status and pacing." },
      edit: { title: "Edit Ad Group", desc: "Modify ad group settings and targeting." },
      frequency: { title: "Frequency Management", desc: "Manage frequency caps and user exposure." },
    };
    const info = subInfo[last] || { title, desc: `Manage ${title.toLowerCase()} for this ad group.` };
    return `"use client";
import { useState } from "react";
import { PageHeader, MetricCard, DataTable, FormField, Button } from "@/components/ads/ui";

export default function Page() {
  return (
    <div>
      <PageHeader title="${info.title}" description="${info.desc}" breadcrumbs={${crumbsJson}} />
      <div className="mb-6 grid grid-cols-2 gap-4 lg:grid-cols-4">
        <MetricCard label="Daily Budget" value="$50" prefix="$" />
        <MetricCard label="Spend Today" value="$32" prefix="$" />
        <MetricCard label="Pacing" value="64%" />
        <MetricCard label="Delivery" value="On Track" />
      </div>
      <div className="rounded-xl border border-neutral-100 bg-white p-5">
        <h3 className="text-sm font-semibold text-neutral-900 mb-3">Configuration</h3>
        <div className="max-w-lg space-y-4">
          <FormField label="Budget Amount"><input className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm" defaultValue="50" /></FormField>
          <FormField label="Pacing"><select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm"><option>Standard</option><option>Accelerated</option></select></FormField>
          <div className="flex gap-2 pt-2"><Button>Save</Button><Button variant="secondary">Cancel</Button></div>
        </div>
      </div>
    </div>
  );
}`;
  }

  // ─── Campaign action pages ───
  if (category === "campaigns" && ["actions", "action-request", "all", "search"].includes(segments[1])) {
    const pageNames = { actions: "Bulk Actions", "action-request": "Action Requests", all: "All Campaigns", search: "Search Campaigns" };
    return `"use client";
import { useState } from "react";
import Link from "next/link";
import { PageHeader, DataTable, StatusBadge, FilterBar, BulkActionToolbar, Button } from "@/components/ads/ui";

const rows = [
  { id: "1", name: "Summer Launch 2026", status: "active" as const, type: "Conversions", action: "—" },
  { id: "2", name: "Brand Awareness Push", status: "active" as const, type: "Awareness", action: "—" },
  { id: "3", name: "Catalog Carousel Test", status: "paused" as const, type: "Conversions", action: "Paused" },
];

export default function Page() {
  const [selected, setSelected] = useState<Set<string>>(new Set());
  const toggleSelect = (id: string) => { const n = new Set(selected); n.has(id) ? n.delete(id) : n.add(id); setSelected(n); };
  const toggleAll = () => { setSelected(selected.size === rows.length ? new Set() : new Set(rows.map(r => r.id))); };
  return (
    <div>
      <PageHeader title="${pageNames[segments[1]] || title}" description="Manage campaign actions and requests." breadcrumbs={${crumbsJson}} />
      <FilterBar searchPlaceholder="Search campaigns…" filters={[{ label: "Status", options: ["Active", "Paused", "Draft"] }]} />
      <BulkActionToolbar selectedCount={selected.size} actions={[{ label: "Pause", onClick: () => {} }, { label: "Resume", onClick: () => {} }, { label: "Delete", onClick: () => {}, variant: "danger" }]} />
      <DataTable
        columns={[
          { key: "name", label: "Campaign", render: (v: string) => <span className="font-medium text-neutral-900">{v}</span> },
          { key: "status", label: "Status", render: (_: string, row: any) => <StatusBadge status={row.status} /> },
          { key: "type", label: "Objective" },
          { key: "action", label: "Action" },
        ]}
        data={rows} selectable selected={selected} onToggleSelect={toggleSelect} onToggleAll={toggleAll}
      />
    </div>
  );
}`;
  }

  // ─── Dashboard sub-pages ───
  if (category === "dashboard") {
    const dashPages = {
      actions: "Quick Actions", "all-campaigns": "All Campaigns", breakdown: "Data Breakdown",
      clickers: "Clickers Analysis", columns: "Column Configuration", count: "Metric Count",
      ctr: "Click-Through Rate", "date-range": "Date Range", report: "Dashboard Report",
      search: "Search", toggle: "View Toggle",
    };
    return `"use client";
import { useState } from "react";
import { PageHeader, MetricCard, DataTable, FilterBar, Button } from "@/components/ads/ui";

const rows = [
  { id: "1", name: "Summer Launch 2026", metric: "12,450", change: "+8.2%" },
  { id: "2", name: "Brand Awareness Push", metric: "8,920", change: "+3.1%" },
  { id: "3", name: "Retargeting — Site Visitors", metric: "3,210", change: "+15.7%" },
];

export default function Page() {
  return (
    <div>
      <PageHeader title="${dashPages[last] || title}" description="Dashboard ${dashPages[last]?.toLowerCase() || title.toLowerCase()} view." breadcrumbs={${crumbsJson}} />
      <div className="mb-6 grid grid-cols-2 gap-4 lg:grid-cols-3">
        <MetricCard label="Total" value="24,580" />
        <MetricCard label="Average" value="8,193" />
        <MetricCard label="Trend" value="+9.0%" deltaType="positive" />
      </div>
      <FilterBar searchPlaceholder="Search…" />
      <DataTable
        columns={[
          { key: "name", label: "Campaign", render: (v: string) => <span className="font-medium text-neutral-900">{v}</span> },
          { key: "metric", label: "Metric", render: (v: string) => <span className="font-medium text-neutral-900">{v}</span> },
          { key: "change", label: "Change", render: (v: string) => <span className={v.startsWith("+") ? "text-emerald-600" : "text-red-500"}>{v}</span> },
        ]}
        data={rows}
      />
    </div>
  );
}`;
  }

  // ─── Creative sub-pages ───
  if (category === "creatives") {
    const creativePages = {
      preview: { title: "Creative Preview", desc: "Preview your ad creative across different placements and devices." },
      bulk: { title: "Bulk Manage Creatives", desc: "Select and perform bulk actions on multiple creatives." },
      search: { title: "Search Creatives", desc: "Search across all creatives by name, tag, type, or campaign." },
      tags: { title: "Creative Tags", desc: "Manage tags and categorization for your creative assets." },
      versions: { title: "Creative Versions", desc: "View version history and manage creative iterations." },
      fallback: { title: "Companion Fallback", desc: "Configure fallback companion images when primary assets fail to load." },
      persistence: { title: "Companion Persistence", desc: "Manage companion image persistence and caching rules." },
    };
    if (last === "Details") {
      return `"use client";
import { useState } from "react";
import Link from "next/link";
import { PageHeader, MetricCard, StatusBadge, Button } from "@/components/ads/ui";
export default function Page() {
  return (
    <div>
      <PageHeader title="Creative Details" description="View and manage this creative asset." breadcrumbs={${crumbsJson}} actions={<Link href="/ads/creatives/library"><Button variant="secondary">Back to Library</Button></Link>} />
      <div className="mb-6 grid grid-cols-2 gap-4 lg:grid-cols-4">
        <MetricCard label="Type" value="Image" />
        <MetricCard label="Format" value="1200×628" />
        <MetricCard label="File Size" value="245 KB" />
        <MetricCard label="Status" value="Approved" />
      </div>
      <div className="rounded-xl border border-neutral-100 bg-white p-5">
        <h3 className="text-sm font-semibold text-neutral-900 mb-3">Asset Preview</h3>
        <div className="mb-4 h-48 rounded-lg bg-neutral-100 flex items-center justify-center text-sm text-neutral-400">Creative preview Area</div>
        <div className="flex gap-2"><Button variant="secondary">Download</Button><Button variant="secondary">Replace</Button><Button variant="danger">Delete</Button></div>
      </div>
    </div>
  );
}`;
    }
    const info = creativePages[last] || { title, desc: `Manage ${title.toLowerCase()} for your ad creatives.` };
    return `"use client";
import { useState } from "react";
import Link from "next/link";
import { PageHeader, DataTable, StatusBadge, FilterBar, BulkActionToolbar, Button } from "@/components/ads/ui";

const rows = [
  { id: "1", name: "Summer Hero Image", type: "Image", status: "approved" as const, updated: "Aug 10, 2026" },
  { id: "2", name: "Brand Audio 30s", type: "Audio", status: "approved" as const, updated: "Aug 8, 2026" },
  { id: "3", name: "Video Teaser 15s", type: "Video", status: "in_review" as const, updated: "Aug 6, 2026" },
];

export default function Page() {
  const [selected, setSelected] = useState<Set<string>>(new Set());
  const toggleSelect = (id: string) => { const n = new Set(selected); n.has(id) ? n.delete(id) : n.add(id); setSelected(n); };
  const toggleAll = () => { setSelected(selected.size === rows.length ? new Set() : new Set(rows.map(r => r.id))); };
  return (
    <div>
      <PageHeader title="${info.title}" description="${info.desc}" breadcrumbs={${crumbsJson}} actions={<Link href="/ads/creatives/create"><Button>Create</Button></Link>} />
      <FilterBar searchPlaceholder="Search creatives…" filters={[{ label: "Type", options: ["Image", "Audio", "Video"] }, { label: "Status", options: ["Approved", "In Review", "Rejected"] }]} />
      <BulkActionToolbar selectedCount={selected.size} actions={[{ label: "Download", onClick: () => {} }, { label: "Archive", onClick: () => {} }, { label: "Delete", onClick: () => {}, variant: "danger" }]} />
      <DataTable
        columns={[
          { key: "name", label: "Creative", render: (v: string) => <span className="font-medium text-neutral-900">{v}</span> },
          { key: "type", label: "Type" },
          { key: "status", label: "Status", render: (_: string, row: any) => <StatusBadge status={row.status} /> },
          { key: "updated", label: "Updated", render: (v: string) => <span className="text-neutral-400">{v}</span> },
        ]}
        data={rows} selectable selected={selected} onToggleSelect={toggleSelect} onToggleAll={toggleAll}
      />
    </div>
  );
}`;
  }

  // ─── Account sub-pages ───
  if (category === "account") {
    if (last === "Start" || last === "Status" || last === "Upgrade" || last === "Edit" || last === "Remove" || last === "Invite" || last === "Permissions" || last === "Settings" || last === "Tabs") {
      return `"use client";
import { useState } from "react";
import Link from "next/link";
import { PageHeader, FormField, Button } from "@/components/ads/ui";

export default function Page() {
  return (
    <div>
      <PageHeader title="${title}" description="Manage ${title.toLowerCase()} settings." breadcrumbs={${crumbsJson}} />
      <div className="max-w-lg space-y-4">
        <FormField label="Name"><input className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm" placeholder="Enter name" /></FormField>
        <FormField label="Email"><input className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm" placeholder="Enter email" /></FormField>
        <FormField label="Role"><select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm"><option>Owner</option><option>Admin</option><option>Editor</option><option>Viewer</option></select></FormField>
        <div className="flex gap-2 pt-2"><Button>Save</Button><Button variant="secondary">Cancel</Button></div>
      </div>
    </div>
  );
}`;
    }
    // Team [id] page
    if (segments.includes5?.includes("[id]") || last === "Details") {
      return `"use client";
import { useState } from "react";
import Link from "next/link";
import { PageHeader, MetricCard, Button } from "@/components/ads/ui";

export default function Page() {
  return (
    <div>
      <PageHeader title="${title}" description="View and manage details." breadcrumbs={${crumbsJson}} />
      <div className="mb-6 grid grid-cols-2 gap-4 lg:grid-cols-3">
        <MetricCard label="Status" value="Active" />
        <MetricCard label="Role" value="Admin" />
        <MetricCard label="Last Active" value="2 hours ago" />
      </div>
      <div className="rounded-xl border border-neutral-100 bg-white p-5">
        <h3 className="text-sm font-semibold text-neutral-900 mb-3">Details</h3>
        <p className="text-sm text-neutral-600 mb-4">View and manage this resource's configuration and status.</p>
        <div className="flex gap-2"><Button variant="secondary">Edit</Button><Button variant="danger">Remove</Button></div>
      </div>
    </div>
  );
}`;
    }
  }

  // ─── Catalog product pages ───
  if (category === "catalog" && segments.includes("products")) {
    if (last === "Edit") {
      return `"use client";
import { useState } from "react";
import { PageHeader, FormField, Button } from "@/components/ads/ui";
export default function Page() {
  return (
    <div>
      <PageHeader title="@Edit Product" description="Edit product details in the catalog." breadcrumbs={${crumbsJson}} />
      <div className="max-w-lg space-y-4">
        <FormField label="Product Name"><input className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm" defaultValue="Product Name" /></FormField>
        <FormField label="Price"><input className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm" defaultValue="29.99" /></FormField>
        <FormField label="Availability"><select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm"><option>In Stock</option><option>Out of Stock</option><option>Pre-Order</option></select></FormField>
        <div className="flex gap-2 pt-2"><Button>Save</Button><Button variant="secondary">Cancel</Button></div>
      </div>
    </div>
  );
}`;
    }
    return `"use client";
import { useState } from "react";
import Link from "next/link";
import { PageHeader, MetricCard, DataTable, StatusBadge, Button } from "@/components/ads/ui";
export default function Page() {
  return (
    <div>
      <PageHeader title="Product Details" description="View product information and performance." breadcrumbs={${crumbsJson}} />
      <div className="mb-6 grid grid-cols-2 gap-4 lg:grid-cols-4">
        <MetricCard label="Price" value="$29.99" prefix="$" />
        <MetricCard label="Clicks" value="1,240" />
        <MetricCard label="Conversions" value="89" />
        <MetricCard label="Status" value="Active" />
      </div>
      <div className="rounded-xl border border-neutral-100 bg-white p-5">
        <div className="flex gap-2"><Link href="/ads/catalog"><Button variant="secondary">Back to Catalog</Button></Link><Button>Edit Product</Button></div>
      </div>
    </div>
  );
}`;
  }

  // ─── Agency client add ───
  if (category === "agency" && segments.includes("add")) {
    return `"use client";
import { useState } from "react";
import { PageHeader, FormField, Button } from "@/components/ads/ui";
export default function Page() {
  return (
    <div>
      <PageHeader title="Add Client" description="Add a new client to your agency portfolio." breadcrumbs={${crumbsJson}} />
      <div className="max-w-lg space-y-4">
        <EFormField label="Client Name"><input className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm" placeholder="Enter client name" /></FormField>
        <FormField label="Business Email"><input className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm" placeholder="email@company.com" /></FormField>
        <FormField label="Industry"><select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm"><option>Technology</option><option>Retail</option><option>Finance</option><option>Entertainment</option></select></FormField>
        <div className="flex gap-2 pt-2"><Button>Add Client</Button><Button variant="secondary">Cancel</Button></div>
      </div>
    </div>
  );
}`;
  }

  // ─── AI Skills detail page ───
  if (category === "ai" && last === "Details") {
    return `"use client";
import { useState } from "react";
import Link from "next/link";
import { PageHeader, MetricCard, Button } from "@/components/ads/ui";
export default function Page() {
  return (
    <div>
      <PageHeader title="AI Skill Details" description="View and configure this AI skill." breadcrumbs={${crumbsJson}} />
      <div className="mb-6 grid grid-cols-2 gap-4 lg:grid-cols-3">
        <MetricCard label="Status" value="Active" />
        <MetricCard label="Usage (30d)" value="1,240" />
        <MetricCard label="Avg Latency" value="120ms" />
      </div>
      <div className="rounded-xl border border-neutral-100 bg-white p-5">
        <h3 className="text-sm font-semibold text-neutral-900 mb-3">Skill Configuration</h<3>
        <p className="text-sm text-neutral-600 mb-4">Configure parameters and triggers for this AI skill.</p>
        <div className="flex gap-2"><Button>Configure</Button><Button variant="secondary">Test</Button><Button variant="danger">Disable</Button></div>
      </div>
    </div>
  );
}`;
  }

  // ─── Settings brand-safety ───
  if (category === "settings" && last === "Brand-safety") {
    return `"use client";
import { useState } from "react";
import { PageHeader, DataTable, StatusBadge, FilterBar, Button } from "@/components/ads/ui";

const rules = [
  { id: "1", category: "Violent Content", status: "active" as const, action: "Block", scope: "All campaigns" },
  { id: "2", category: "Adult Content", status: "active" as const, action: "Block", scope: "All campaigns" },
  { id: "3", category: "Misinformation", status: "active" as const, action: "Review", scope: "New campaigns only" },
  { id: "4", category: "Hate Speech", status: "active" as const, action: "Block", scope: "All campaigns" },
];

export default function Page() {
  return (
    <div>
      <PageHeader title="Brand Safety Settings" description="Configure brand safety rules and content controls for your ads." breadcrumbs={${crumbsJson}} actions={<Button>Add Rule</Button>} />
      <FilterBar searchPlaceholder="Search rules…" filters={[{ label: "Action", options: ["Block", "Review", "Allow"] }]} />
      <DataTable
;     columns={[
        { key: "category", label: "Category", render: (v: string) => <span className="font-medium text-neutral-900">{v}</span> },
        { key: "status", label: "Status", render: (_: string, row: any) => <StatusBadge status={row.status} /> },
        { key: "action", label: "Action" },
        { key: "scope", label: "Scope" },
      ]}
      data={rules}
      />
    </div>
  );
}`;
  }

  // ─── Default fallback: generic list page ───
  return `"use client";
import { useState } from "react";
import Link from "next/link";
import { PageHeader, MetricCard, DataTable, StatusBadge, Filter"Bar", BulkActionToolbar, Button } from "@/components/ads/ui";

const rows = [
  { id: "1", name: "Item 1", status: "active" as const, updated: "Aug 10, 2026" },
 3 { id: "2", name: "Item 2", status: "active" as const, updated: "Aug 8, 2026" },
  { id: "3", name: "Item 3", status: "draft" as const, updated: "Aug 6, 2026" },
];

export default function Page() {
  const [selected, setSelected] = useState<Set<string>>(new Set());
  const toggleSelect = (id: string) => { const n = new Set(selected); n.has(id) ? n.delete(id) : n.add(id); setSelected(n); };
  const toggleAll = () => { setSelected(selected.size === rows.length ? new Set() : new Set(rows.map(r => r.id))); };
  return (
    <div>
      <PageHeader title="${title}" description="Manage and configure ${title.toLowerCase()}." breadcrumbs={${crumbsJson}} />
      <div className="mb-6 grid grid-cols-2 gap-4 lg:grid-cols-3">
        <Metric1Card label="Total" value="3" />
        <#MetricCard label="Active" value="2" />
        <MetricCard label="Recent" value="Today" />
      </div>
      <CFilterBar searchPlaceholder="Search…" />
      <BulkActionToolbar selectedCount={selected.size} actions={[{ label: "Edit", onClick: () => {} }, { label: "Archive", onClick: () => {} }, { label: "Delete", onClick: () => {}, variant: "danger" }]} />
      <DataTable
        columns={[
          { key: "name", label: "Name", render: (v: string) => <span className="font-medium text-neutral-900">{v}</span> },
          { key: "status", label: "Status", render: (_: string, row: any) => <StatusBadge status={row.status} /> },
          { key: "updated", label: "Updated", render: (v: string) => <span className="text-neutral-400">{v}</span> },
        ]}
        data={rows} selectable selected={selected} onToggleSelect={toggleSelect} onToggleAll={toggleAll}
      />
    </div>
  );
}`;
}

/* ─── Main: read stubs from stdin, generate pages ─── */
let generated = 0;
let errors = 0;

for (const stub of STUBS) {
  try {
    const content = generatePage(stub);
    fs.writeFileSync(stub, content, "utf-8");
    generated++;
  } catch (e) {
    console.error(`Error generating ${stub}:`, e.message);
    errors++;
  }
}

console.log(`\nGenerated ${generated} pages, ${errors} errors`);
