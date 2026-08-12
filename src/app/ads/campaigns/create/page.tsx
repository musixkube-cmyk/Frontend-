"use client";

import { useState } from "react";
import Link from "next/link";

const steps = ["Objective", "Campaign", "Ad Group", "Ad", "Review"];

const objectives = [
  { category: "Awareness", items: ["Reach", "Video Views"] },
  { category: "Consideration", items: ["Traffic", "Community Interaction", "Brand Consideration", "Music Streams"] },
  { category: "Conversion", items: ["App Promotion", "Lead Generation", "Sales"] },
];

export default function CreateCampaign() {
  const [step, setStep] = useState(0);
  const [objective, setObjective] = useState("");
  const [campaignName, setCampaignName] = useState("");
  const [dailyBudget, setDailyBudget] = useState("50");
  const [budgetType, setBudgetType] = useState("daily");

  return (
    <div>
      {/* Stepper */}
      <div className="mb-8 flex items-center gap-2">
        {steps.map((s, i) => (
          <div key={s} className="flex items-center gap-2">
            <button
              onClick={() => i <= step && setStep(i)}
              className={`flex h-8 w-8 items-center justify-center rounded-full text-xs font-semibold transition-colors ${
                i < step ? "bg-neutral-900 text-white" : i === step ? "border-2 border-neutral-900 text-neutral-900" : "border border-neutral-300 text-neutral-400"
              }`}
            >
              {i < step ? "✓" : i + 1}
            </button>
            <span className={`text-sm ${i === step ? "font-medium text-neutral-900" : "text-neutral-400"}`}>{s}</span>
            {i < steps.length - 1 && <div className="mx-2 h-px w-8 bg-neutral-200" />}
          </div>
        ))}
      </div>

      <div className="flex gap-6">
        {/* Main form area */}
        <div className="flex-1">
          {/* Step 0: Objective */}
          {step === 0 && (
            <div>
              <h2 className="text-xl font-bold text-neutral-900 mb-1">Choose an objective</h2>
              <p className="text-sm text-neutral-500 mb-6">Your objective determines how your ads are optimized and delivered.</p>
              <div className="space-y-6">
                {objectives.map((cat) => (
                  <div key={cat.category}>
                    <h3 className="text-xs font-semibold uppercase tracking-wider text-neutral-400 mb-3">{cat.category}</h3>
                    <div className="grid grid-cols-2 gap-3">
                      {cat.items.map((item) => (
                        <button
                          key={item}
                          onClick={() => setObjective(item)}
                          className={`rounded-xl border p-4 text-left text-sm transition-colors ${
                            objective === item ? "border-neutral-900 bg-neutral-50 font-medium text-neutral-900" : "border-neutral-200 text-neutral-700 hover:border-neutral-300"
                          }`}
                        >
                          {item}
                        </button>
                      ))}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Step 1: Campaign */}
          {step === 1 && (
            <div>
              <h2 className="text-xl font-bold text-neutral-900 mb-1">Campaign settings</h2>
              <p className="text-sm text-neutral-500 mb-6">Name your campaign and configure budget and delivery.</p>
              <div className="space-y-5">
                <div>
                  <label className="block text-sm font-medium text-neutral-700 mb-1">Campaign name</label>
                  <input value={campaignName} onChange={(e) => setCampaignName(e.target.value)} placeholder="e.g. Summer Launch 2026" className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900 focus:border-neutral-400 focus:outline-none" />
                </div>
                <div>
                  <label className="block text-sm font-medium text-neutral-700 mb-1">Special ad category</label>
                  <select className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900 focus:border-neutral-400 focus:outline-none">
                    <option>None</option><option>Housing</option><option>Credit</option><option>Employment</option><option>Politics</option>
                  </select>
                </div>
                <div>
                  <label className="block text-sm font-medium text-neutral-700 mb-2">Budget type</label>
                  <div className="flex gap-2">
                    <button onClick={() => setBudgetType("daily")} className={`rounded-lg px-4 py-2 text-sm font-medium transition-colors ${budgetType === "daily" ? "bg-neutral-900 text-white" : "border border-neutral-200 text-neutral-700"}`}>Daily</button>
                    <button onClick={() => setBudgetType("lifetime")} className={`rounded-lg px-4 py-2 text-sm font-medium transition-colors ${budgetType === "lifetime" ? "bg-neutral-900 text-white" : "border border-neutral-200 text-neutral-700"}`}>Lifetime</button>
                  </div>
                </div>
                <div>
                  <label className="block text-sm font-medium text-neutral-700 mb-1">{budgetType === "daily" ? "Daily budget" : "Lifetime budget"}</label>
                  <div className="relative">
                    <span className="absolute left-3 top-1/2 -translate-y-1/2 text-sm text-neutral-400">$</span>
                    <input value={dailyBudget} onChange={(e) => setDailyBudget(e.target.value)} type="number" className="w-full rounded-lg border border-neutral-200 py-2.5 pl-7 pr-3 text-sm text-neutral-900 focus:border-neutral-400 focus:outline-none" />
                  </div>
                </div>
                <div>
                  <label className="block text-sm font-medium text-neutral-700 mb-1">Delivery type</label>
                  <select className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900 focus:border-neutral-400 focus:outline-none">
                    <option>Standard</option><option>Accelerated</option>
                  </select>
                </div>
              </div>
            </div>
          )}

          {/* Step 2: Ad Group */}
          {step === 2 && (
            <div>
              <h2 className="text-xl font-bold text-neutral-900 mb-1">Ad group configuration</h2>
              <p className="text-sm text-neutral-500 mb-6">Define audience, placements, and optimization for this ad group.</p>
              <div className="space-y-5">
                <div>
                  <label className="block text-sm font-medium text-neutral-700 mb-1">Ad group name</label>
                  <input defaultValue="Ad Group 1" className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900 focus:border-neutral-400 focus:outline-none" />
                </div>
                <div>
                  <label className="block text-sm font-medium text-neutral-700 mb-1">Locations</label>
                  <input defaultValue="United States" className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900 focus:border-neutral-400 focus:outline-none" />
                </div>
                <div className="grid grid-cols-2 gap-4">
                  <div>
                    <label className="block text-sm font-medium text-neutral-700 mb-1">Age range</label>
                    <select className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900 focus:border-neutral-400 focus:outline-none">
                      <option>18–55</option><option>18–24</option><option>25–34</option><option>35–54</option><option>55+</option>
                    </select>
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-neutral-700 mb-1">Gender</label>
                    <select className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900 focus:border-neutral-400 focus:outline-none">
                      <option>All</option><option>Male</option><option>Female</option>
                    </select>
                  </div>
                </div>
                <div>
                  <label className="block text-sm font-medium text-neutral-700 mb-2">Placements</label>
                  <div className="flex flex-wrap gap-2">
                    {["In-Feed Audio", "In-Feed Video", "Top Feed", "Search Ads", "Catalog Ads"].map((p) => (
                      <button key={p} className="rounded-lg border border-neutral-200 px-3 py-1.5 text-xs font-medium text-neutral-700 transition-colors hover:border-neutral-300">{p}</button>
                    ))}
                  </div>
                </div>
                <div>
                  <label className="block text-sm font-medium text-neutral-700 mb-1">Optimization goal</label>
                  <select className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900 focus:border-neutral-400 focus:outline-none">
                    <option>Maximize clicks</option><option>Maximize conversions</option><option>Maximize reach</option>
                  </select>
                </div>
              </div>
            </div>
          )}

          {/* Step 3: Ad */}
          {step === 3 && (
            <div>
              <h2 className="text-xl font-bold text-neutral-900 mb-1">Ad creative</h2>
              <p className="text-sm text-neutral-500 mb-6">Choose or create your ad creative, set CTA and destination.</p>
              <div className="space-y-5">
                <div>
                  <label className="block text-sm font-medium text-neutral-700 mb-1">Ad name</label>
                  <input defaultValue="Ad 1" className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900 focus:border-neutral-400 focus:outline-none" />
                </div>
                <div>
                  <label className="block text-sm font-medium text-neutral-700 mb-2">Audio</label>
                  <div className="flex items-center justify-center rounded-xl border-2 border-dashed border-neutral-200 p-8 text-sm text-neutral-400">
                    <div className="text-center">
                      <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" className="mx-auto mb-2 text-neutral-300"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" /><polyline points="17 8 12 3 7 8" /><line x1="12" y1="3" x2="12" y2="15" /></svg>
                      Drag audio file or click to upload
                    </div>
                  </div>
                </div>
                <div>
                  <label className="block text-sm font-medium text-neutral-700 mb-2">Companion image</label>
                  <div className="flex items-center justify-center rounded-xl border-2 border-dashed border-neutral-200 p-8 text-sm text-neutral-400">
                    Upload companion image (1200×628)
                  </div>
                </div>
                <div className="grid grid-cols-2 gap-4">
                  <div>
                    <label className="block text-sm font-medium text-neutral-700 mb-1">CTA</label>
                    <select className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900 focus:border-neutral-400 focus:outline-none">
                      <option>Learn More</option><option>Shop Now</option><option>Listen Now</option><option>Download</option><option>Sign Up</option>
                    </select>
                  </div>
                  <div>
                    <label className="block text-sm font-medium text-neutral-700 mb-1">Destination URL</label>
                    <input placeholder="https://..." className="w-full rounded-lg border border-neutral-200 px-3 py-2.5 text-sm text-neutral-900 focus:border-neutral-400 focus:outline-none" />
                  </div>
                </div>
              </div>
            </div>
          )}

          {/* Step 4: Review */}
          {step === 4 && (
            <div>
              <h2 className="text-xl font-bold text-neutral-900 mb-1">Review & publish</h2>
              <p className="text-sm text-neutral-500 mb-6">Confirm your campaign configuration before publishing.</p>
              <div className="space-y-4">
                <div className="rounded-xl border border-neutral-100 bg-white p-5">
                  <h3 className="text-xs font-semibold uppercase tracking-wider text-neutral-400 mb-3">Campaign</h3>
                  <div className="grid grid-cols-2 gap-y-2 text-sm">
                    <span className="text-neutral-500">Name</span><span className="text-neutral-900 font-medium">{campaignName || "Untitled"}</span>
                    <span className="text-neutral-500">Objective</span><span className="text-neutral-900 font-medium">{objective || "Not selected"}</span>
                    <span className="text-neutral-500">Budget</span><span className="text-neutral-900 font-medium">${dailyBudget}/{budgetType === "daily" ? "day" : "lifetime"}</span>
                  </div>
                </div>
                <div className="rounded-xl border border-neutral-100 bg-white p-5">
                  <h3 className="text-xs font-semibold uppercase tracking-wider text-neutral-400 mb-3">Policy check</h3>
                  <p className="text-sm text-emerald-600">No issues found. Campaign is ready to publish.</p>
                </div>
              </div>
            </div>
          )}
        </div>

        {/* Right context panel — estimates & policy */}
        {step >= 1 && (
          <div className="hidden w-72 shrink-0 lg:block">
            <div className="rounded-xl border border-neutral-100 bg-white p-5">
              <h3 className="text-sm font-semibold text-neutral-900 mb-3">Estimated results</h3>
              <div className="space-y-3 text-sm">
                <div className="flex justify-between"><span className="text-neutral-500">Reach</span><span className="font-medium text-neutral-900">~24K</span></div>
                <div className="flex justify-between"><span className="text-neutral-500">Impressions</span><span className="font-medium text-neutral-900">~42K</span></div>
                <div className="flex justify-between"><span className="text-neutral-500">Clicks</span><span className="font-medium text-neutral-900">~520</span></div>
                <div className="flex justify-between"><span className="text-neutral-500">CPA</span><span className="font-medium text-neutral-900">~$9.60</span></div>
              </div>
            </div>
          </div>
        )}
      </div>

      {/* Footer actions */}
      <div className="mt-8 flex items-center justify-between border-t border-neutral-200 pt-4">
        <button
          onClick={() => step > 0 && setStep(step - 1)}
          className={`text-sm font-medium ${step > 0 ? "text-neutral-700" : "text-neutral-300"}`}
          disabled={step === 0}
        >
          Back
        </button>
        <div className="flex gap-3">
          <button className="rounded-lg border border-neutral-200 px-4 py-2 text-sm font-medium text-neutral-700">Save draft</button>
          {step < 4 ? (
            <button onClick={() => setStep(step + 1)} className="rounded-lg bg-neutral-900 px-4 py-2 text-sm font-medium text-white transition-colors hover:bg-neutral-800">Continue</button>
          ) : (
            <button className="rounded-lg bg-neutral-900 px-6 py-2 text-sm font-medium text-white transition-colors hover:bg-neutral-800">Publish</button>
          )}
        </div>
      </div>
    </div>
  );
}
