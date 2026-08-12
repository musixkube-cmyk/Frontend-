"use client";

import Link from "next/link";

export default function Page() {
  return (
    <div>
      <div className="mb-6 flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold tracking-tight text-neutral-900">Audiences</h1>
          <p className="mt-1 text-sm text-neutral-500">Create and manage reusable audiences — custom, lookalike, artist affinity, demographics.</p>
        </div>
                <Link
          href="/ads/audiences/create"
          className="flex h-9 items-center gap-2 rounded-lg bg-neutral-900 px-4 text-sm font-medium text-white transition-colors hover:bg-neutral-800"
        >
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M12 5v14M5 12h14" /></svg>
          Create Audience
        </Link>
      </div>

      <div className="rounded-xl border border-neutral-100 bg-white">
        <table className="w-full">
          <thead>
            <tr className="border-b border-neutral-100 text-left text-xs font-medium uppercase tracking-wider text-neutral-400">
              <th className="px-4 py-3">Audience</th>
              <th className="px-4 py-3">Type</th>
              <th className="px-4 py-3">Size</th>
              <th className="px-4 py-3">Status</th>
              <th className="px-4 py-3">Last updated</th>
            </tr>
          </thead>
          <tbody>
            <tr className="border-b border-neutral-50">
                <td className="px-4 py-3 text-sm text-neutral-700">Broad US 18-55</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Demographic</td>
                <td className="px-4 py-3 text-sm text-neutral-700">~42M</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Ready</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Aug 10, 2026</td>
            </tr>
            <tr className="border-b border-neutral-50">
                <td className="px-4 py-3 text-sm text-neutral-700">Custom — Past Purchasers</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Custom</td>
                <td className="px-4 py-3 text-sm text-neutral-700">~12K</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Ready</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Aug 8, 2026</td>
            </tr>
            <tr className="border-b border-neutral-50">
                <td className="px-4 py-3 text-sm text-neutral-700">Lookalike — Purchasers 1%</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Lookalike</td>
                <td className="px-4 py-3 text-sm text-neutral-700">~2.1M</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Ready</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Aug 5, 2026</td>
            </tr>
            <tr className="border-b border-neutral-50">
                <td className="px-4 py-3 text-sm text-neutral-700">Artist Affinity — EDM</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Artist Affinity</td>
                <td className="px-4 py-3 text-sm text-neutral-700">~890K</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Ready</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Aug 1, 2026</td>
            </tr>
            <tr className="border-b border-neutral-50">
                <td className="px-4 py-3 text-sm text-neutral-700">Exclude — Employees</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Exclusion</td>
                <td className="px-4 py-3 text-sm text-neutral-700">~450</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Ready</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Jul 30, 2026</td>
            </tr>

          </tbody>
        </table>
      </div>
    </div>
  );
}
