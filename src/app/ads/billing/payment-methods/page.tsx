"use client";

import Link from "next/link";

export default function Page() {
  return (
    <div>
      <div className="mb-6 flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold tracking-tight text-neutral-900">Payment Methods</h1>
          <p className="mt-1 text-sm text-neutral-500">Manage credit cards, debit cards, and other payment methods.</p>
        </div>
                <Link
          href="/ads/billing/payment-methods/add"
          className="flex h-9 items-center gap-2 rounded-lg bg-neutral-900 px-4 text-sm font-medium text-white transition-colors hover:bg-neutral-800"
        >
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M12 5v14M5 12h14" /></svg>
          Add Payment Method
        </Link>
      </div>

      <div className="rounded-xl border border-neutral-100 bg-white">
        <table className="w-full">
          <thead>
            <tr className="border-b border-neutral-100 text-left text-xs font-medium uppercase tracking-wider text-neutral-400">
              <th className="px-4 py-3">Method</th>
              <th className="px-4 py-3">Type</th>
              <th className="px-4 py-3">Last 4</th>
              <th className="px-4 py-3">Expiry</th>
              <th className="px-4 py-3">Default</th>
            </tr>
          </thead>
          <tbody>
            <tr className="border-b border-neutral-50">
                <td className="px-4 py-3 text-sm text-neutral-700">Visa ending 4242</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Credit card</td>
                <td className="px-4 py-3 text-sm text-neutral-700">4242</td>
                <td className="px-4 py-3 text-sm text-neutral-700">12/27</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Yes</td>
            </tr>
            <tr className="border-b border-neutral-50">
                <td className="px-4 py-3 text-sm text-neutral-700">Mastercard ending 8888</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Credit card</td>
                <td className="px-4 py-3 text-sm text-neutral-700">8888</td>
                <td className="px-4 py-3 text-sm text-neutral-700">06/26</td>
                <td className="px-4 py-3 text-sm text-neutral-700">No</td>
            </tr>

          </tbody>
        </table>
      </div>
    </div>
  );
}
