"use client";

import Link from "next/link";

export default function Page() {
  return (
    <div>
      <div className="mb-6 flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold tracking-tight text-neutral-900">Instant Forms</h1>
          <p className="mt-1 text-sm text-neutral-500">Create and manage lead generation forms.</p>
        </div>
                <Link
          href="#"
          className="flex h-9 items-center gap-2 rounded-lg bg-neutral-900 px-4 text-sm font-medium text-white transition-colors hover:bg-neutral-800"
        >
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M12 5v14M5 12h14" /></svg>
          Create Form
        </Link>
      </div>

      <div className="rounded-xl border border-neutral-100 bg-white">
        <table className="w-full">
          <thead>
            <tr className="border-b border-neutral-100 text-left text-xs font-medium uppercase tracking-wider text-neutral-400">
              <th className="px-4 py-3">Form</th>
              <th className="px-4 py-3">Leads</th>
              <th className="px-4 py-3">Conversion rate</th>
              <th className="px-4 py-3">Status</th>
              <th className="px-4 py-3">Last updated</th>
            </tr>
          </thead>
          <tbody>
            <tr className="border-b border-neutral-50">
                <td className="px-4 py-3 text-sm text-neutral-700">Summer Lead Form</td>
                <td className="px-4 py-3 text-sm text-neutral-700">234</td>
                <td className="px-4 py-3 text-sm text-neutral-700">8.2%</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Active</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Aug 10, 2026</td>
            </tr>
            <tr className="border-b border-neutral-50">
                <td className="px-4 py-3 text-sm text-neutral-700">Newsletter Signup</td>
                <td className="px-4 py-3 text-sm text-neutral-700">1,420</td>
                <td className="px-4 py-3 text-sm text-neutral-700">12.4%</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Active</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Aug 1, 2026</td>
            </tr>
            <tr className="border-b border-neutral-50">
                <td className="px-4 py-3 text-sm text-neutral-700">Demo Request</td>
                <td className="px-4 py-3 text-sm text-neutral-700">56</td>
                <td className="px-4 py-3 text-sm text-neutral-700">3.1%</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Paused</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Jul 15, 2026</td>
            </tr>

          </tbody>
        </table>
      </div>
    </div>
  );
}
