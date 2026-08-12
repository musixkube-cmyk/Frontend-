"use client";

import Link from "next/link";

export default function Page() {
  return (
    <div>
      <div className="mb-6 flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold tracking-tight text-neutral-900">Notifications</h1>
          <p className="mt-1 text-sm text-neutral-500">Review and resolve account events.</p>
        </div>
        
      </div>

      <div className="rounded-xl border border-neutral-100 bg-white">
        <table className="w-full">
          <thead>
            <tr className="border-b border-neutral-100 text-left text-xs font-medium uppercase tracking-wider text-neutral-400">
              <th className="px-4 py-3">Type</th>
              <th className="px-4 py-3">Message</th>
              <th className="px-4 py-3">Time</th>
              <th className="px-4 py-3">Status</th>
            </tr>
          </thead>
          <tbody>
            <tr className="border-b border-neutral-50">
                <td className="px-4 py-3 text-sm text-neutral-700">Issue</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Campaign budget exhausted</td>
                <td className="px-4 py-3 text-sm text-neutral-700">2 min ago</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Unresolved</td>
            </tr>
            <tr className="border-b border-neutral-50">
                <td className="px-4 py-3 text-sm text-neutral-700">Announcement</td>
                <td className="px-4 py-3 text-sm text-neutral-700">New placement: Top Feed Video</td>
                <td className="px-4 py-3 text-sm text-neutral-700">1 hour ago</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Read</td>
            </tr>
            <tr className="border-b border-neutral-50">
                <td className="px-4 py-3 text-sm text-neutral-700">Suggestion</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Increase budget on Summer Launch for 15% more reach</td>
                <td className="px-4 py-3 text-sm text-neutral-700">3 hours ago</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Pending</td>
            </tr>
            <tr className="border-b border-neutral-50">
                <td className="px-4 py-3 text-sm text-neutral-700">Ticket</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Creative rejected — policy violation</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Yesterday</td>
                <td className="px-4 py-3 text-sm text-neutral-700">Open</td>
            </tr>

          </tbody>
        </table>
      </div>
    </div>
  );
}
