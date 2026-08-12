"use client";

import Link from "next/link";

export default function Page() {
  return (
    <div>
      <div className="mb-6 flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold tracking-tight text-neutral-900">Leads Center</h1>
          <p className="mt-1 text-sm text-neutral-500">Filter, search, export, respond to, and qualify leads.</p>
        </div>
                <Link
          href="/ads/leads/export"
          className="flex h-9 items-center gap-2 rounded-lg bg-neutral-900 px-4 text-sm font-medium text-white transition-colors hover:bg-neutral-800"
        >
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M12 5v14M5 12h14" /></svg>
          Export Leads
        </Link>
      </div>

      <div className="rounded-xl border border-neutral-100 bg-white">
        <table className="w-full">
          <thead>
            <tr className="border-b border-neutral-100 text-left text-xs font-medium uppercase tracking-wider text-neutral-400">
              <th className="px-4 py-3">Lead</th>
              <th className="px-4 py-3">Source</th>
              <th className="px-4 py-3">Campaign</th>
              <th className="px-4 py-3">Status</th>
              <th className="px-4 py-3">Created</th>
              <th className="px-4 py-3">Value</th>
            </tr>
          </thead>
          <tbody>
            <tr className="border-b border-neutral-50">
                <td className="px-4 py-3 text-sm text-neutral-700">Sarah Chen</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Instant Form</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Summer Launch 2026</td>
                <td className="px-4 py-3 text-sm text-neutral-700">New</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Aug 12, 2026</td>
                <td className="px-4 py-3 text-sm text-neutral-700">$120</td>
            </tr>
            <tr className="border-b border-neutral-50">
                <td className="px-4 py-3 text-sm text-neutral-700">Marcus Johnson</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Direct Message</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Brand Awareness Push</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Contacted</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Aug 11, 2026</td>
                <td className="px-4 py-3 text-sm text-neutral-700">$85</td>
            </tr>
            <tr className="border-b border-neutral-50">
                <td className="px-4 py-3 text-sm text-neutral-700">Emily Rodriguez</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Website Form</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Summer Launch 2026</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Qualified</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Aug 10, 2026</td>
                <td className="px-4 py-3 text-sm text-neutral-700">$200</td>
            </tr>
            <tr className="border-b border-neutral-50">
                <td className="px-4 py-3 text-sm text-neutral-700">David Kim</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Instant Form</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Summer Launch 2026</td>
                <td className="px-4 py-3 text-sm text-neutral-700">New</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Aug 9, 2026</td>
                <td className="px-4 py-3 text-sm text-neutral-700">$95</td>
            </tr>

          </tbody>
        </table>
      </div>
    </div>
  );
}
