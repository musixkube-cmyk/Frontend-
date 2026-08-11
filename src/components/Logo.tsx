import Link from "next/link";

export function Logo({ className = "h-8" }: { className?: string }) {
  return (
    <Link href="/" className="inline-flex items-center" aria-label="Musicosy home">
      <svg
        viewBox="0 0 180 36"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
        className={`${className} w-auto`}
        aria-hidden="true"
      >
        {/* Orange accent dot */}
        <circle cx="12" cy="18" r="6" fill="oklch(0.72 0.19 45)" />
        {/* Brand text */}
        <text
          x="24"
          y="26"
          fontFamily="var(--font-display), 'Space Grotesk', system-ui, sans-serif"
          fontSize="24"
          fontWeight="700"
          fill="currentColor"
          letterSpacing="-0.02em"
        >
          musicosy
        </text>
      </svg>
    </Link>
  );
}
