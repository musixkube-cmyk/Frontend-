"use client";

import { useEffect, useRef } from "react";

/**
 * Animated starfield background that replaces the astronaut video.
 * Renders a canvas of twinkling stars with a slow drift animation
 * plus a CSS nebula gradient overlay — evoking a deep-space feel.
 */
export function Starfield() {
  const canvasRef = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    const STAR_COUNT = 280;
    let animId = 0;

    interface Star {
      x: number;
      y: number;
      r: number;
      speed: number;
      phase: number;
    }

    const stars: Star[] = Array.from({ length: STAR_COUNT }, () => ({
      x: Math.random(),
      y: Math.random(),
      r: Math.random() * 1.5 + 0.3,
      speed: Math.random() * 0.3 + 0.1,
      phase: Math.random() * Math.PI * 2,
    }));

    function resize() {
      if (!canvas) return;
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
    }

    function draw(t: number) {
      if (!ctx || !canvas) return;
      const w = canvas.width;
      const h = canvas.height;
      ctx.clearRect(0, 0, w, h);

      for (const s of stars) {
        const brightness = 0.35 + 0.65 * Math.sin(s.speed * t * 0.001 + s.phase);
        ctx.beginPath();
        ctx.arc(s.x * w, s.y * h, s.r, 0, Math.PI * 2);
        ctx.fillStyle = `rgba(255,255,255,${brightness})`;
        ctx.fill();
      }
      animId = requestAnimationFrame(draw);
    }

    resize();
    window.addEventListener("resize", resize);
    animId = requestAnimationFrame(draw);

    return () => {
      window.removeEventListener("resize", resize);
      cancelAnimationFrame(animId);
    };
  }, []);

  return (
    <div className="fixed inset-0 -z-10">
      {/* Star canvas */}
      <canvas ref={canvasRef} className="h-full w-full" aria-hidden="true" />
      {/* Dark overlay with gradient — matches original bg-ink/70 + gradient */}
      <div className="absolute inset-0 bg-ink/70" />
      <div className="absolute inset-0 bg-gradient-to-r from-ink via-ink/50 to-ink/20" />
      {/* Nebula glow */}
      <div
        className="absolute inset-0 opacity-30"
        style={{
          background:
            "radial-gradient(ellipse 80% 60% at 20% 50%, oklch(0.25 0.06 45 / 0.6), transparent), radial-gradient(ellipse 60% 50% at 80% 40%, oklch(0.2 0.04 260 / 0.4), transparent)",
          animation: "nebula-shift 25s ease-in-out infinite",
          backgroundSize: "200% 200%",
        }}
        aria-hidden="true"
      />
    </div>
  );
}
