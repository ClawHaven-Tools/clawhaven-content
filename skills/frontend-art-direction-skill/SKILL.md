---
name: frontend-skill
description: Design visually strong landing pages, websites, apps, and UI with premium art direction, hierarchy, restraint, imagery, and motion. Use when quality depends on composition and visual narrative rather than component count, including full-bleed hero pages, product surfaces, and motion-led interfaces.
---

# Frontend Skill

Ship interfaces that feel deliberate, premium, and current.

## Working model

Before building, define:

1. visual thesis: one sentence for mood, material, energy.
2. content plan: hero, support, detail, final CTA.
3. interaction thesis: 2-3 motion ideas that change page feel.

Assign one job per section, one dominant visual idea, one primary takeaway/action.

## Beautiful defaults

- Start from composition, not components.
- Prefer full-bleed hero or full-canvas visual anchor.
- Make brand/product name the loudest text.
- Keep copy short and scannable.
- Use whitespace, alignment, scale, cropping, contrast before extra chrome.
- Limit system to 2 typefaces max and 1 accent color by default.
- Default to cardless layouts.
- Treat first viewport as a poster, not a document.

## Landing page structure

Default sequence:

1. Hero: brand/product, promise, CTA, one dominant visual.
2. Support: one concrete feature/offer/proof point.
3. Detail: atmosphere/workflow/depth/story.
4. Final CTA: convert/start/visit/contact.

### Hero rules

- Keep one composition only.
- Use full-bleed image or dominant visual plane.
- Keep hero edge-to-edge on branded landing pages; constrain only inner text/action column.
- Keep hierarchy: brand first, headline second, body third, CTA fourth.
- Avoid hero cards, stat strips, logo clouds, pill soup, floating dashboards by default.
- Keep headline around 2-3 lines desktop and one-glance readable on mobile.
- Keep text column narrow on calm image area.
- Ensure strong text contrast and clear tap targets.

### Viewport budget

- Count sticky/fixed header as part of first-screen budget.
- Fit header + hero into initial viewport on desktop/mobile.
- When using 100vh/100svh, subtract persistent UI chrome (`calc(100svh - header-height)`) or overlay header.

## App UI defaults

Apply Linear-style restraint:

- calm surface hierarchy,
- strong typography/spacing,
- few colors,
- dense but readable information,
- minimal chrome,
- use cards only when card itself is interaction.

Organize around:

- primary workspace,
- navigation,
- secondary context/inspector,
- one clear accent for action/state.

Avoid dashboard card mosaics, heavy borders everywhere, decorative gradients behind routine UI, competing accents, ornamental icons.

## Imagery rules

- Use imagery for narrative work.
- Use at least one strong real-looking image for brand/venue/editorial/lifestyle pages.
- Prefer in-situ photography over abstract filler.
- Choose/crop stable tonal area for text.
- Avoid embedded signage/logos/typographic clutter in image.
- Avoid generated images with built-in UI frames/splits/cards/panels.
- Use multiple images for multiple moments, not one collage.
- Keep a real visual anchor in first viewport.

## Copy rules

- Write product language, not design commentary.
- Let headline carry meaning.
- Keep support copy to one short sentence when possible.
- Remove repetition across sections.
- Remove prompt/meta commentary from UI text.
- Give every section one responsibility: explain, prove, deepen, or convert.
- Keep deleting if removing 30% improves clarity.

## Utility copy mode (product surfaces)

When building dashboard/app/admin/operations UI:

- Prioritize orientation, status, action.
- Start with working surface (KPIs, charts, filters, tables, status, tasks).
- Avoid hero unless explicitly requested.
- Use operational headings: "Selected KPIs", "Plan status", "Top segments", "Last sync".
- Avoid aspirational homepage-like language unless requested.
- Keep support text to scope/behavior/freshness/decision value in one sentence.
- Remove any section that does not help operate, monitor, or decide.

## Motion rules

Use motion for presence and hierarchy, not noise.

Ship at least 2-3 intentional motions for visually-led work:

1. one hero entrance sequence,
2. one scroll-linked/sticky/depth effect,
3. one hover/reveal/layout transition improving affordance.

Prefer Framer Motion (when available) for reveals, shared layout transitions, scroll transforms, sticky storytelling, narrative carousels, drawer/modal presence effects.

Require motion to be visible in quick recording, smooth on mobile, fast, restrained, consistent, and removed if ornamental only.

## Hard rules

- Use no cards by default.
- Use no hero cards by default.
- Use no boxed/center-column hero for full-bleed briefs.
- Keep one dominant idea per section.
- Avoid many tiny UI devices to explain one section.
- Keep brand prominence above headline on branded pages.
- Use no filler copy.
- Use no split-screen hero unless text sits on calm unified side.
- Use max two typefaces unless clear reason.
- Use max one accent color unless existing strong product system.

## Reject failures

- generic SaaS card grid as first impression,
- beautiful image with weak brand presence,
- strong headline with unclear action,
- busy imagery behind text,
- repeated mood statements across sections,
- purposeless carousel,
- app UI as stacked cards instead of layout.

## Litmus checks

Before finalizing, verify:

1. Is brand/product unmistakable in first screen?
2. Is there one strong visual anchor?
3. Can page be understood by scanning headlines only?
4. Does each section have one job?
5. Are cards actually necessary?
6. Does motion improve hierarchy/atmosphere?
7. Does design still feel premium without decorative shadows?
