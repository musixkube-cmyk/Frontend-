export type Entry = {
  slug: string;
  num: string;
  label: string;
  headline: string;
  sub: string;
};

export const entries: Entry[] = [
  {
    slug: "stream",
    num: "01",
    label: "Stream",
    headline: "YOUR SOUND FIRST",
    sub: "Sign in to start listening the way it was meant to be heard.",
  },
  {
    slug: "earn",
    num: "02",
    label: "Earn",
    headline: "GET PAID PLAYING",
    sub: "Sign in to track payouts, splits and every stream you own.",
  },
  {
    slug: "publish",
    num: "03",
    label: "Publish",
    headline: "MADE TO BE FOUND",
    sub: "Sign in to push your release everywhere at once.",
  },
  {
    slug: "create",
    num: "04",
    label: "Create",
    headline: "BUILT TO RELEASE",
    sub: "Sign in to move from session file to finished record.",
  },
  {
    slug: "engage",
    num: "05",
    label: "Engage",
    headline: "HEARD. NOT SCROLLED.",
    sub: "Sign in to talk to the people actually playing you.",
  },
  {
    slug: "manage",
    num: "06",
    label: "Manage",
    headline: "RUN YOUR CATALOG",
    sub: "Sign in to keep rights, metadata and masters in order.",
  },
  {
    slug: "grow",
    num: "07",
    label: "Grow",
    headline: "FIND YOUR PEOPLE",
    sub: "Sign in to turn listeners into a following.",
  },
];

export const entryBySlug = (slug: string) => entries.find((e) => e.slug === slug);
