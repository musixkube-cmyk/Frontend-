"use client";

export default function AccountBusinessPage() {
  return (
    <div>
      <div className="mb-6">
        <h1 className="text-2xl font-bold tracking-tight text-neutral-900">Account & Business</h1>
        <p className="mt-1 text-sm text-neutral-500">Manage your advertiser account and business information.</p>
      </div>
      <div className="space-y-6">
        <div className="rounded-xl border border-neutral-100 bg-white p-6">
          <h3 className="text-sm font-semibold text-neutral-900 mb-4">Business information</h3>
          <div className="grid gap-4 lg:grid-cols-2">
            <div><label className="block text-sm text-neutral-600 mb-1">Business name</label><input defaultValue="Acme Music Group" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900" /></div>
            <div><label className="block text-sm text-neutral-600 mb-1">Industry</label><select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900"><option>Music & Entertainment</option><option>Technology</option><option>Retail</option></select></div>
            <div><label className="block text-sm text-neutral-600 mb-1">Country</label><input defaultValue="United States" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900" /></div>
            <div><label className="block text-sm text-neutral-600 mb-1">Website</label><input defaultValue="https://acmemusic.com" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900" /></div>
          </div>
        </div>
        <div className="rounded-xl border border-neutral-100 bg-white p-6">
          <h3 className="text-sm font-semibold text-neutral-900 mb-4">Advertiser account</h3>
          <div className="grid gap-4 lg:grid-cols-3">
            <div><label className="block text-sm text-neutral-600 mb-1">Account name</label><input defaultValue="Acme Ads" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900" /></div>
            <div><label className="block text-sm text-neutral-600 mb-1">Time zone</label><select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900"><option>America/Chicago (CDT)</option></select></div>
            <div><label className="block text-sm text-neutral-600 mb-1">Currency</label><select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900"><option>USD</option><option>EUR</option><option>GBP</option></select></div>
          </div>
        </div>
        <div className="flex justify-end"><button className="rounded-lg bg-neutral-900 px-4 py-2 text-sm font-medium text-white">Save</button></div>
      </div>
    </div>
  );
}
