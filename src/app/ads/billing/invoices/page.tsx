"use client";

import Link from "next/link";

export default function Page() {
  return (
    <div>
      <div className="mb-6 flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold tracking-tight text-neutral-900">Invoices</h1>
          <p className="mt-1 text-sm text-neutral-500">View and download invoices.</p>
        </div>
        
      </div>

      <div className="rounded-xl border border-neutral-100 bg-white">
        <table className="w-full">
          <thead>
            <tr className="border-b border-neutral-100 text-left text-xs font-medium uppercase tracking-wider text-neutral-400">
              <th className="px-4 py-3">Invoice</th>
              <th className="px-4 py-3">Date</th>
              <th className="px-4 py-3">Amount</th>
              <th className="px-4 py-3">Status</th>
              <th className="px-4 py-3">Due date</th>
            </tr>
          </thead>
          <tbody>
            <tr className="border-b border-neutral-50">
                <td className="px-4 py-3 text-sm text-neutral-700">INV-2026-08</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Aug 1, 2026</td>
                <td className="px-4 py-3 text-sm text-neutral-700">$3,680.00</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Paid</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Aug 15, 2026</td>
            </tr>
            <tr className="border-b border-neutral-50">
                <td className="px-4 py-3 text-sm text-neutral-700">INV-2026-07</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Jul 1, 2026</td>
                <td className="px-4 py-3 text-sm text-neutral-700">$2,140.00</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Paid</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Jul 15, 2026</td>
            </tr>
            <tr className="border-b border-neutral-50">
                <td className="px-4 py-3 text-sm text-neutral-700">INV-2026-06</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Jun 1, 2026</td>
                <td className="px-4 py-3 text-sm text-neutral-700">$1,890.00</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Paid</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Jun 15, 2026</td>
            </tr>

          </tbody>
        </table>
      </div>
    </div>
  );
}
