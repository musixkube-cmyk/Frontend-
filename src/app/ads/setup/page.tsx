"use client";

import { useState } from "react";
import { PageHeader, Button, FormField } from "@/components/ads/ui";

const STEPS = ["Business Info", "Account Type", "Payment", "Targeting Defaults", "Team Members", "Review"];

export default function SetupPage() {
  const [step, setStep] = useState(0);
  const [businessName, setBusinessName] = useState("");
  const [industry, setIndustry] = useState("");
  const [accountType, setAccountType] = useState("advertiser");
  const [paymentMethod, setPaymentMethod] = useState("credit-card");

  return (
    <div className="mx-auto max-w-3xl p-6">
      <PageHeader
        title="Account Setup"
        description={`Step ${step + 1} of 6 — ${STEPS[step]}`}
      />

      {/* Progress bar */}
      <div className="mb-8 flex items-center gap-1">
        {STEPS.map((s, i) => (
          <div key={s} className="flex items-center gap-1">
            <div className={`flex h-8 w-8 items-center justify-center rounded-full text-xs font-semibold ${
              i === step ? "bg-neutral-900 text-white" : i < step ? "bg-emerald-500 text-white" : "bg-neutral-100 text-neutral-400"
            }`}>
              {i + 1}
            </div>
            {i < STEPS.length - 1 && <div className={`h-0.5 w-8 ${i < step ? "bg-emerald-500" : "bg-neutral-100"}`} />}
          </div>
        ))}
      </div>

      <div className="rounded-xl border border-neutral-100 bg-white p-6">
        {/* Step 1: Business Info */}
        {step === 0 && (
          <div className="space-y-4">
            <h2 className="text-lg font-semibold text-neutral-900">Business Information</h2>
            <FormField label="Business Name">
              <input value={businessName} onChange={(e) => setBusinessName(e.target.value)} placeholder="Your company name" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900 placeholder:text-neutral-400 focus:border-neutral-400 focus:outline-none" />
            </FormField>
            <FormField label="Industry">
              <select value={industry} onChange={(e) => setIndustry(e.target.value)} className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-700 focus:border-neutral-400 focus:outline-none">
                <option value="">Select industry…</option>
                <option>Music & Entertainment</option><option>Technology</option><option>Retail & E-commerce</option><option>Financial Services</option><option>Healthcare</option><option>Education</option><option>Other</option>
              </select>
            </FormField>
            <FormField label="Business Website">
              <input placeholder="https://yourcompany.com" className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900 placeholder:text-neutral-400 focus:border-neutral-400 focus:outline-none" />
            </FormField>
          </div>
        )}

        {/* Step 2: Account Type */}
        {step === 1 && (
          <div className="space-y-4">
            <h2 className="text-lg font-semibold text-neutral-900">Account Type</h2>
            <div className="grid grid-cols-1 gap-4 sm:grid-cols-2">
              {[
                { id: "advertiser", label: "Advertiser", desc: "Run ads for your own business" },
                { id: "agency", label: "Agency", desc: "Manage ads for multiple clients" },
              ].map((t) => (
                <button key={t.id} onClick={() => setAccountType(t.id)} className={`rounded-xl border-2 p-5 text-left ${accountType === t.id ? "border-neutral-900 bg-neutral-50" : "border-neutral-100"}`}>
                  <h3 className="text-sm font-semibold text-neutral-900">{t.label}</h3>
                  <p className="mt-1 text-xs text-neutral-500">{t.desc}</p>
                </button>
              ))}
            </div>
          </div>
        )}

        {/* Step 3: Payment */}
        {step === 2 && (
          <div className="space-y-4">
            <h2 className="text-lg font-semibold text-neutral-900">Payment Method</h2>
            <div className="grid grid-cols-1 gap-3 sm:grid-cols-3">
              {[
                { id: "credit-card", label: "Credit Card", desc: "Visa, Mastercard, Amex" },
                { id: "bank-transfer", label: "Bank Transfer", desc: "ACH or wire transfer" },
                { id: "invoice", label: "Invoice", desc: "Monthly invoicing (qualified)" },
              ].map((m) => (
                <button key={m.id} onClick={() => setPaymentMethod(m.id)} className={`rounded-xl border-2 p-4 text-left ${paymentMethod === m.id ? "border-neutral-900 bg-neutral-50" : "border-neutral-100"}`}>
                  <h3 className="text-sm font-semibold text-neutral-900">{m.label}</h3>
                  <p className="mt-1 text-xs text-neutral-500">{m.desc}</p>
                </button>
              ))}
            </div>
          </div>
        )}

        {/* Step 4: Targeting Defaults */}
        {step === 3 && (
          <div className="space-y-4">
            <h2 className="text-lg font-semibold text-neutral-900">Default Targeting</h2>
            <FormField label="Default Geographic Target">
              <select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-700 focus:border-neutral-400 focus:outline-none">
                <option>United States</option><option>Canada</option><option>United Kingdom</option><option>European Union</option><option>Worldwide</option>
              </select>
            </FormField>
            <FormField label="Default Language">
              <select className="w-full rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-700 focus:border-neutral-400 focus:outline-none">
                <option>English</option><option>Spanish</option><option>French</option><option>German</option><option>All Languages</option>
              </select>
            </FormField>
            <FormField label="Default Age Range">
              <div className="flex gap-2">
                <select className="rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-700 focus:border-neutral-400 focus:outline-none">
                  <option>18</option><option>21</option><option>25</option>
                </select>
                <span className="py-2 text-sm text-neutral-400">to</span>
                <select className="rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-700 focus:border-neutral-400 focus:outline-none">
                  <option>34</option><option>44</option><option>54</option><option>65+</option>
                </select>
              </div>
            </FormField>
          </div>
        )}

        {/* Step 5: Team Members */}
        {step === 4 && (
          <div className="space-y-4">
            <h2 className="text-lg font-semibold text-neutral-900">Team Members</h2>
            <p className="text-sm text-neutral-500">Invite team members to help manage your advertising account.</p>
            <FormField label="Invite by Email">
              <div className="flex gap-2">
                <input placeholder="colleague@company.com" className="flex-1 rounded-lg border border-neutral-200 px-3 py-2 text-sm text-neutral-900 placeholder:text-neutral-400 focus:border-neutral-400 focus:outline-none" />
                <Button variant="secondary">Invite</Button>
              </div>
            </FormField>
            <div className="rounded-lg border border-neutral-100 p-4 text-sm text-neutral-500">
              You are the account owner. You can add more team members later from Account Settings.
            </div>
          </div>
        )}

        {/* Step 6: Review */}
        {step === 5 && (
          <div className="space-y-4">
            <h2 className="text-lg font-semibold text-neutral-900">Review Setup</h2>
            <div className="space-y-3 rounded-lg border border-neutral-100 p-4">
              <div className="flex justify-between text-sm"><span className="text-neutral-500">Business:</span><span className="font-medium text-neutral-900">{businessName || "—"}</span></div>
              <div className="flex justify-between text-sm"><span className="text-neutral-500">Industry:</span><span className="font-medium text-neutral-900">{industry || "—"}</span></div>
              <div className="flex justify-between text-sm"><span className="text-neutral-500">Account Type:</span><span className="font-medium text-neutral-900 capitalize">{accountType}</span></div>
              <div className="flex justify-between text-sm"><span className="text-neutral-500">Payment:</span><span className="font-medium text-neutral-900">{paymentMethod.replace("-", " ")}</span></div>
            </div>
          </div>
        )}
      </div>

      <div className="mt-6 flex items-center justify-between">
        <Button variant="ghost" onClick={() => setStep(Math.max(0, step - 1))} disabled={step === 0}>Back</Button>
        {step < STEPS.length - 1 ? (
          <Button onClick={() => setStep(Math.min(STEPS.length - 1, step + 1))}>Continue</Button>
        ) : (
          <Button onClick={() => window.location.href = "/ads/dashboard"}>Complete Setup</Button>
        )}
      </div>
    </div>
  );
}
