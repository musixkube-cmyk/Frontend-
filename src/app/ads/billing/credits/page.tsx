"use client";

import Link from "next/link";

export default function Page() {
  return (
    <div>
      <div className="mb-6 flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold tracking-tight text-neutral-900">Credits & Promotions</h1>
          <p className="mt-1 text-sm text-neutral-500">View ad credits, promotional offers, and rebates.</p>
        </div>
        
      </div>

      <div className="rounded-xl border border-neutral-100 bg-white">
        <table className="w-full">
          <thead>
            <tr className="border-b border-neutral-100 text-left text-xs font-medium uppercase tracking-wider text-neutral-400">
              <th className="px-4 py-3">Credit</th>
              <th className="px-4 py-3">Type</th>
              <th className="px-4 py-3">Amount</th>
              <th className="px-4 py-3">Expires</th>
              <th className="px-4 py-3">Status</th>
            </tr>
          </thead>
          <tbody>
            <tr className="border-b border-neutral-50">
                <td className="px-4 py-3 text-sm text-neutral-700">Welcome credit</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Promotional</td>
                <td className="px-4 py-3 text-sm text-neutral-700">$500.00</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Dec 31, 2026</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Active</td>
            </tr>
            <tr className="border-b border-neutral-50">
                <td className="px-4 py-3 text-sm text-neutral-700">Spend match Q3</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Match</td>
                <td className="px-4 py-3 text-sm text-neutral-700">$250.00</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Sep 30, 2026</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Active</td>
            </tr>

          </tbody>
        </table>
      </div>
    </div>
  );
}
