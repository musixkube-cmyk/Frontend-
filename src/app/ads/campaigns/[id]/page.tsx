"use client";

import Link from "next/link";
import { use } from "react";

export default function CampaignDetail({ params }: { params: Promise<{ id: string }> }) {
  const { id } = use(params);
  return (
    <div>
      <div className="mb-6">
        <div className="flex items-center gap-2 text-sm text-neutral-500">
          <Link href="/ads/campaigns" className="hover:text-neutral-900">Campaigns</Link>
          <span>/</span>
          <span className="text-neutral-900">Campaign {id}</span>
        </div>
        <div className="mt-3 flex items-center justify-between">
          <div>
            <h1 className="text-2xl font-bold tracking-tight text-neutral-900">Summer Launch 2026</h1>
            <div className="mt-2 flex items-center gap-3">
              <span className="inline-flex items-center rounded-full bg-emerald-50 px-2.5 py-0.5 text-xs font-medium text-emerald-700">Active</span>
              <span className="text-sm text-neutral-500">Conversions · Daily budget $100</span>
            </div>
          </div>
          <div className="flex items-center gap-2">
            <button className="rounded-lg border border-neutral-200 px-4 py-2 text-sm font-medium text-neutral-700 transition-colors hover:bg-neutral-50">Pause</button>
            <button className="rounded-lg border border-neutral-200 px-4 py-2 text-sm font-medium text-neutral-700 transition-colors hover:bg-neutral-50">Duplicate</button>
            <Link href={`/ads/campaigns/${id}/edit`} className="rounded-lg bg-neutral-900 px-4 py-2 text-sm font-medium text-white transition-colors hover:bg-neutral-800">Edit</Link>
          </div>
        </div>
      </div>

      {/* Tabs */}
      <div className="mb-6 flex gap-1 border-b border-neutral-200">
        {["Overview", "Ad Groups", "Ads", "Analytics", "Settings", "Activity"].map((tab, i) => (
          <button key={tab} className={`px-4 py-2.5 text-sm font-medium transition-colors ${i === 0 ? "border-b-2 border-neutral-900 text-neutral-900" : "text-neutral-500 hover:text-neutral-700"}`}>
            {tab}
          </button>
        ))}
      </div>

      {/* KPI row */}
      <div className="mb-6 grid grid-cols-2 gap-4 lg:grid-cols-4">
        {[
          { label: "Spend", value: "$2,450" },
          { label: "Impressions", value: "89.2K" },
          { label: "Clicks", value: "1,230" },
          { label: "Conversions", value: "186" },
        ].map((kpi) => (
          <div key={kpi.label} className="rounded-xl border border-neutral-100 bg-white p-5">
            <p className="text-xs font-medium uppercase tracking-wider text-neutral-400">{kpi.label}</p>
            <p className="mt-2 text-2xl font-bold text-neutral-900">{kpi.value}</p>
          </div>
        ))}
      </div>

      {/* Ad Groups table */}
      <div className="rounded-xl border border-neutral-100 bg-white">
        <div className="border-b border-neutral-100 px-5 py-4">
          <h2 className="text-sm font-semibold text-neutral-900">Ad Groups</h2>
        </div>
        <table className="w-full">
          <thead>
            <tr className="border-b border-neutral-100 text-left text-xs font-medium uppercase tracking-wider text-neutral-400">
              <th className="px-5 py-3">Ad Group</th>
              <th className="px-5 py-3">Status</th>
              <th className="px-5 py-3">Budget</th>
              <th className="px-5 py-3">Spend</th>
              <th className="px-5 py-3">Results</th>
            </tr>
          </thead>
          <tbody>
            <tr className="border-b border-neutral-50 text-sm">
              <td className="px-5 py-4 font-medium text-neutral-900">Audio — Broad Audience</td>
              <td className="px-5 py-4"><span className="inline-flex items-center rounded-full bg-emerald-50 px-2 py-0.5 text-xs font-medium text-emerald-700">Active</span></td>
              <td className="px-5 py-4 text-neutral-700">$50/day</td>
              <td className="px-5 py-4 text-neutral-900">$1,520</td>
              <td className="px-5 py-4 text-neutral-700">842 clicks</td>
            </tr>
            <tr className="text-sm">
              <td className="px-5 py-4 font-medium text-neutral-900">Video — Retarget</td>
              <td className="px-5 py-4"><span className="inline-flex items-center rounded-full bg-emerald-50 px-2 py-0.5 text-xs font-medium text-emerald-700">Active</span></td>
              <td className="px-5 py-4 text-neutral-700">$50/day</td>
              <td className="px-5 py-4 text-neutral-900">$930</td>
              <td className="px-5 py-4 text-neutral-700">388 clicks</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
}
