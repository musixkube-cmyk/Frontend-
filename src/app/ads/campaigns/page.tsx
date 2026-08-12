"use client";

import Link from "next/link";

export default function Page() {
  return (
    <div>
      <div className="mb-6 flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold tracking-tight text-neutral-900">All Campaigns</h1>
          <p className="mt-1 text-sm text-neutral-500">Find, compare, pause, duplicate, edit, and report on campaigns.</p>
        </div>
                <Link
          href="/ads/campaigns/create"
          className="flex h-9 items-center gap-2 rounded-lg bg-neutral-900 px-4 text-sm font-medium text-white transition-colors hover:bg-neutral-800"
        >
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M12 5v14M5 12h14" /></svg>
          Create Campaign
        </Link>
      </div>

      <div className="rounded-xl border border-neutral-100 bg-white">
        <table className="w-full">
          <thead>
            <tr className="border-b border-neutral-100 text-left text-xs font-medium uppercase tracking-wider text-neutral-400">
              <th className="px-4 py-3">Campaign</th>
              <th className="px-4 py-3">Status</th>
              <th className="px-4 py-3">Objective</th>
              <th className="px-4 py-3">Spend</th>
              <th className="px-4 py-3">Results</th>
              <th className="px-4 py-3">Date range</th>
            </tr>
          </thead>
          <tbody>
            <tr className="border-b border-neutral-50">
                <td className="px-4 py-3 text-sm text-neutral-700">Summer Launch 2026</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Active</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Conversions</td>
                <td className="px-4 py-3 text-sm text-neutral-700">$2,450</td>
                <td className="px-4 py-3 text-sm text-neutral-700">1,230 clicks</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Jul 15 – Aug 12</td>
            </tr>
            <tr className="border-b border-neutral-50">
                <td className="px-4 py-3 text-sm text-neutral-700">Brand Awareness Push</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Active</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Awareness</td>
                <td className="px-4 py-3 text-sm text-neutral-700">$890</td>
                <td className="px-4 py-3 text-sm text-neutral-700">45K impressions</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Aug 1 – Aug 31</td>
            </tr>
            <tr className="border-b border-neutral-50">
                <td className="px-4 py-3 text-sm text-neutral-700">Catalog Carousel Test</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Paused</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Conversions</td>
                <td className="px-4 py-3 text-sm text-neutral-700">$340</td>
                <td className="px-4 py-3 text-sm text-neutral-700">89 clicks</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Jun 20 – Jul 5</td>
            </tr>
            <tr className="border-b border-neutral-50">
                <td className="px-4 py-3 text-sm text-neutral-700">Artist Spotlight Q3</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Draft</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Consideration</td>
                <td className="px-4 py-3 text-sm text-neutral-700">$0</td>
                <td className="px-4 py-3 text-sm text-neutral-700">—</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Not set</td>
            </tr>
            <tr className="border-b border-neutral-50">
                <td className="px-4 py-3 text-sm text-neutral-700">Holiday Promo 2025</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Completed</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Sales</td>
                <td className="px-4 py-3 text-sm text-neutral-700">$12,400</td>
                <td className="px-4 py-3 text-sm text-neutral-700">4,200 purchases</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Dec 1 – Dec 31</td>
            </tr>

          </tbody>
        </table>
      </div>
    </div>
  );
}
