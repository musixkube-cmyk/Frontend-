import Link from "next/link";

export function Logo({ className = "h-8" }: { className?: string }) {
  return (
    <Link href="/" className="inline-flex items-center" aria-label="Musicosy home">
      <img
        src="/musicosy-logo.png"
        alt="Musicosy"
        className={`${className} w-auto object-contain`}
        loading="lazy"
      />
    </Link>
  );
}
