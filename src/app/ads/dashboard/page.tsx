"use client";

import { useState } from "react";
import Link from "next/link";
import { PageHeader, MetricCard, DataTable, StatusBadge, TabBar, Button } from "@/components/ads/ui";

const campaigns = [
  { id: "1", name: "Summer Launch 2026", status: "active" as const, objective: "Conversions", budget: "$100/day", spend: "$2,450", results: "1,230 clicks", roas: "3.4x" },
  { id: "2", name: "Brand Awareness Push", status: "active" as const, objective: "Awareness", budget: "$30/day", spend: "$890", results: "45K impressions", roas: "2.1x" },
  { id: "3", name: "Catalog Carousel Test", status: "paused" as const, objective: "Conversions", budget: "$20/day", spend: "$340", results: "89 clicks", roas: "1.8x" },
  { id: "4", name: "Retargeting — Site Visitors", status: "active" as const, objective: "Conversions", budget: "$50/day", spend: "$1,120", results: "340 conversions", roas: "5.2x" },
  { id: "5", name: "Audio Discovery Campaign", status: "draft" as const, objective: "Awareness", budget: "$25/day", spend: "$0", results: "—", roas: "—" },
];

const recentActivity = [
  { id: "a1", action: "paused", user: "Alex Rivera", time: "2 min ago", detail: "Catalog Carousel Test paused due to low CTR" },
  { id: "a2", action: "created", user: "Alex Rivera", time: "1 hour ago", detail: "Audio Discovery Campaign created as draft" },
  { id: "a3", action: "budget changed", user: "Alex Rivera", time: "3 hours ago", detail: "Summer Launch 2026 daily budget increased to $100" },
  { id: "a4", action: "creative rejected", user: "System", time: "5 hours ago", detail: "Companion image in Retargeting ad group failed policy review" },
];

export default function DashboardPage() {
  const [tab, setTab] = useState(0);

  return (
    <div>
      <PageHeader
        title="Dashboard"
        description="Overview of your advertising performance, campaign health, and recent activity."
        breadcrumbs={[{ label: "Ad Center" }, { label: "Dashboard" }]}
        actions={
          <Link href="/ads/ads-manager/campaigns/create">
            <Button>Create Campaign</Button>
          </Link>
        }
      />

      {/* KPI Scorecards */}
      <div className="mb-6 grid grid-cols-2 gap-4 lg:grid-cols-4">
        <MetricCard label="Total Spend" value="$4,800" delta="+12% vs last 30d" deltaType="negative" prefix="$" />
        <MetricCard label="Impressions" value="187K" delta="+8% vs last 30d" deltaType="positive" />
        <MetricCard label="Clicks" value="2,659" delta="+15% vs last 30d" deltaType="positive" />
        <MetricCard label="Conversions" value="526" delta="+22% vs last 30d" deltaType="positive" />
      </div>

      {/* Secondary KPIs */}
      <div className="mb-6 grid grid-cols-2 gap-4 lg:grid-cols-4">
        <MetricCard label="CTR" value="1.42%" delta="+0.12pp" deltaType="positive" />
        <MetricCard label="CPA" value="$9.12" delta="-$1.40" deltaType="positive" prefix="$" />
        <MetricCard label="ROAS" value="3.6x" delta="+0.4x" deltaType="positive" />
        <MetricCard label="Active Campaigns" value="3" delta="of 5 total" deltaType="neutral" />
      </div>

      <TabBar tabs={["Campaigns", "Activity", "Health"]} active={tab} onChange={setTab} />

      {tab === 0 && (
        <div>
          <DataTable
            columns={[
              { key: "name", label: "Campaign", render: (v: string) => <span className="font-medium text-neutral-900">{v}</span> },
              { key: "status", label: "Status", render: (_: string, row: any) => <StatusBadge status={row.status} /> },
              { key: "objective", label: "Objective" },
              { key: "budget", label: "Budget" },
              { key: "spend", label: "Spend", render: (v: string) => <span className="font-medium text-neutral-900">{v}</span> },
              { key: "results", label: "Results" },
              { key: "roas", label: "ROAS", render: (v: string) => <span className="font-medium text-neutral-900">{v}</span> },
            ]}
            data={campaigns}
            rowHref={(row) => `/ads/campaigns/${row.id}`}
          />
        </div>
      )}

      {tab === 1 && (
        <div className="space-y-3">
          {recentActivity.map((item) => (
            <div key={item.id} className="flex items-start gap-3 rounded-xl border border-neutral-100 bg-white p-4">
              <div className="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-neutral-100 text-xs font-semibold text-neutral-600">
                {item.user[0]}
              </div>
              <div className="min-w-0 flex-1">
                <p className="text-sm text-neutral-900">
                  <span className="font-medium">{item.user}</span> {item.action}
                </p>
                <p className="mt-0.5 text-xs text-neutral-500">{item.detail}</p>
                <p className="mt-0.5 text-xs text-neutral-400">{item.time}</p>
              </div>
            </div>
          ))}
        </div>
      )}

      {tab === 2 && (
        <div className="space-y-3">
          <div className="rounded-xl border border-emerald-100 bg-emerald-50 p-4">
            <div className="flex items-center gap-2">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className="text-emerald-600"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14" /><polyline points="22 4 12 14.01 9 11.01" /></svg>
              <span className="text-sm font-medium text-emerald-700">Account Status: Healthy</span>
            </div>
            <p className="mt-1 text-xs text-emerald-600">All systems operational. No policy violations detected. Payment method valid.</p>
          </div>
          <div className="rounded-xl border border-amber-100 bg-amber-50 p-4">
            <div className="flex items-center gap-2">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className="text-amber-600"><circle cx="12" cy="12" r="10" /><line x1="12" y1="8" x2="12" y2="12" /><line x1="12" y1="16" x2="12.01" y2="16" /></svg>
              <span className="text-sm font-medium text-amber-700">1 Creative Under Review</span>
            </div>
            <p className="mt-1 text-xs text-amber-600">A companion image in your Retargeting ad group is pending policy review. Average review time: 24 hours.</p>
          </div>
          <div className="rounded-xl border border-neutral-100 bg-white p-4">
            <div className="flex items-center gap-2">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className="text-neutral-500"><circle cx="12" cy="12" r="10" /><path d="M12 16v-4" /><path d="M12 8h.01" /></svg>
              <span className="text-sm font-medium text-neutral-700">1 Paused Campaign</span>
            </div>
            <p className="mt-1 text-xs text-neutral-500">Catalog Carousel Test was paused due to low CTR. Consider adjusting targeting or creative.</p>
          </div>
        </div>
      )}
    </div>
  );
}
