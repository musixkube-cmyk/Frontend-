"use client";

import Link from "next/link";

export default function Page() {
  return (
    <div>
      <div className="mb-6 flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold tracking-tight text-neutral-900">Drafts</h1>
          <p className="mt-1 text-sm text-neutral-500">Resume incomplete campaign builds.</p>
        </div>
        
      </div>

      <div className="rounded-xl border border-neutral-100 bg-white">
        <table className="w-full">
          <thead>
            <tr className="border-b border-neutral-100 text-left text-xs font-medium uppercase tracking-wider text-neutral-400">
              <th className="px-4 py-3">Draft</th>
              <th className="px-4 py-3">Objective</th>
              <th className="px-4 py-3">Last edited</th>
              <th className="px-4 py-3">Owner</th>
              <th className="px-4 py-3">Status</th>
            </tr>
          </thead>
          <tbody>
            <tr className="border-b border-neutral-50">
                <td className="px-4 py-3 text-sm text-neutral-700">Artist Spotlight Q3</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Consideration</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Aug 10, 2026</td>
                <td className="px-4 py-3 text-sm text-neutral-700">You</td>
                <td className="px-4 py-3 text-sm text-neutral-700">In progress</td>
            </tr>
            <tr className="border-b border-neutral-50">
                <td className="px-4 py-3 text-sm text-neutral-700">Podcast Promo</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Awareness</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Aug 8, 2026</td>
                <td className="px-4 py-3 text-sm text-neutral-700">You</td>
                <td className="px-4 py-3 text-sm text-neutral-700">In progress</td>
            </tr>

          </tbody>
        </table>
      </div>
    </div>
  );
}
