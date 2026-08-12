"use client";

import Link from "next/link";

export default function Page() {
  return (
    <div>
      <div className="mb-6 flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold tracking-tight text-neutral-900">Transactions</h1>
          <p className="mt-1 text-sm text-neutral-500">Review payment history and billing events.</p>
        </div>
        
      </div>

      <div className="rounded-xl border border-neutral-100 bg-white">
        <table className="w-full">
          <thead>
            <tr className="border-b border-neutral-100 text-left text-xs font-medium uppercase tracking-wider text-neutral-400">
              <th className="px-4 py-3">Transaction</th>
              <th className="px-4 py-3">Type</th>
              <th className="px-4 py-3">Amount</th>
              <th className="px-4 py-3">Date</th>
              <th className="px-4 py-3">Status</th>
            </tr>
          </thead>
          <tbody>
            <tr className="border-b border-neutral-50">
                <td className="px-4 py-3 text-sm text-neutral-700">TXN-8924</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Charge</td>
                <td className="px-4 py-3 text-sm text-neutral-700">$120.00</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Aug 12, 2026</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Completed</td>
            </tr>
            <tr className="border-b border-neutral-50">
                <td className="px-4 py-3 text-sm text-neutral-700">TXN-8923</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Charge</td>
                <td className="px-4 py-3 text-sm text-neutral-700">$95.00</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Aug 11, 2026</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Completed</td>
            </tr>
            <tr className="border-b border-neutral-50">
                <td className="px-4 py-3 text-sm text-neutral-700">TXN-8922</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Refund</td>
                <td className="px-4 py-3 text-sm text-neutral-700">$15.00</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Aug 10, 2026</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Completed</td>
            </tr>

          </tbody>
        </table>
      </div>
    </div>
  );
}
