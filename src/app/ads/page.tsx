"use client";

import Link from "next/link";

const campaigns = [
  { id: 1, name: "Summer Launch 2026", status: "Active", objective: "Conversions", spend: "$2,450", results: "1,230 clicks", date: "Jul 15 – Aug 12" },
  { id: 2, name: "Brand Awareness Push", status: "Active", objective: "Awareness", spend: "$890", results: "45K impressions", date: "Aug 1 – Aug 31" },
  { id: 3, name: "Catalog Carousel Test", status: "Paused", objective: "Conversions", spend: "$340", results: "89 clicks", date: "Jun 20 – Jul 5" },
];

export default function AdsDashboard() {
  return (
    <div>
      {/* Header */}
      <div className="mb-6 flex items-center justify-between">
        <div>
          <h1 className="font-display text-2xl font-bold tracking-tight text-neutral-900">
            Ads Manager
          </h1>
          <p className="mt-1 text-sm text-neutral-500">
            Manage your campaigns, creatives, and performance.
          </p>
        </div>
        <Link
          href="/ads/campaign/create"
          className="flex h-10 items-center gap-2 rounded-lg bg-neutral-900 px-5 text-sm font-medium text-white transition-colors hover:bg-neutral-800"
        >
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <path d="M12 5v14M5 12h14" />
          </svg>
          Create
        </Link>
      </div>

      {/* Quick stats */}
      <div className="mb-6 grid grid-cols-1 gap-4 sm:grid-cols-3">
        <div className="rounded-xl border border-neutral-100 bg-white p-5">
          <p className="text-xs font-medium uppercase tracking-wider text-neutral-400">Active campaigns</p>
          <p className="mt-2 font-display text-3xl font-bold text-neutral-900">2</p>
        </div>
        <div className="rounded-xl border border-neutral-100 bg-white p-5">
          <p className="text-xs font-medium uppercase tracking-wider text-neutral-400">Total spend</p>
          <p className="mt-2 font-display text-3xl font-bold text-neutral-900">$3,680</p>
        </div>
        <div className="rounded-xl border border-neutral-100 bg-white p-5">
          <p className="text-xs font-medium uppercase tracking-wider text-neutral-400">Total results</p>
          <p className="mt-2 font-display text-3xl font-bold text-neutral-900">1,319</p>
        </div>
      </div>

      {/* Campaign table */}
      <div className="rounded-xl border border-neutral-100 bg-white">
        <div className="flex items-center justify-between border-b border-neutral-100 px-5 py-4">
          <h2 className="text-sm font-semibold text-neutral-900">Campaigns</h2>
          <Link
            href="/ads/campaigns"
            className="text-xs font-medium text-neutral-500 transition-colors hover:text-neutral-900"
          >
            View all
          </Link>
        </div>
        <table className="w-full">
          <thead>
            <tr className="border-b border-neutral-100 text-left text-xs font-medium uppercase tracking-wider text-neutral-400">
              <th className="px-5 py-3">Campaign</th>
              <th className="px-5 py-3">Status</th>
              <th className="px-5 py-3">Objective</th>
              <th className="px-5 py-3">Spend</th>
              <th className="px-5 py-3">Results</th>
              <th className="px-5 py-3">Date range</th>
            </tr>
          </thead>
          <tbody>
            {campaigns.map((c) => (
              <tr key={c.id} className="border-b border-neutral-50 text-sm last:border-0">
                <td className="px-5 py-4 font-medium text-neutral-900">{c.name}</td>
                <td className="px-5 py-4">
                  <span className={`inline-flex items-center rounded-full px-2 py-0.5 text-xs font-medium ${
                    c.status === "Active" ? "bg-emerald-50 text-emerald-700" : "bg-neutral-100 text-neutral-500"
                  }`}>
                    {c.status}
                  </span>
                </td>
                <td className="px-5 py-4 text-neutral-600">{c.objective}</td>
                <td className="px-5 py-4 text-neutral-900">{c.spend}</td>
                <td className="px-5 py-4 text-neutral-600">{c.results}</td>
                <td className="px-5 py-4 text-neutral-400">{c.date}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
