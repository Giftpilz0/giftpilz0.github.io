import {
  Hct,
  MaterialDynamicColors,
  SchemeTonalSpot,
  argbFromHex,
  hexFromArgb,
  type DynamicColor,
} from "@material/material-color-utilities";

const colors = new MaterialDynamicColors();

/** Exposed as `--md-sys-color-<name>`. */
const ROLES: Record<string, DynamicColor> = {
  primary: colors.primary(),
  "on-primary": colors.onPrimary(),
  "primary-container": colors.primaryContainer(),
  "on-primary-container": colors.onPrimaryContainer(),
  secondary: colors.secondary(),
  "on-secondary": colors.onSecondary(),
  "secondary-container": colors.secondaryContainer(),
  "on-secondary-container": colors.onSecondaryContainer(),
  tertiary: colors.tertiary(),
  "on-tertiary": colors.onTertiary(),
  "tertiary-container": colors.tertiaryContainer(),
  "on-tertiary-container": colors.onTertiaryContainer(),
  error: colors.error(),
  "on-error": colors.onError(),
  "error-container": colors.errorContainer(),
  "on-error-container": colors.onErrorContainer(),
  surface: colors.surface(),
  "on-surface": colors.onSurface(),
  "on-surface-variant": colors.onSurfaceVariant(),
  "surface-container-lowest": colors.surfaceContainerLowest(),
  "surface-container-low": colors.surfaceContainerLow(),
  "surface-container": colors.surfaceContainer(),
  "surface-container-high": colors.surfaceContainerHigh(),
  "surface-container-highest": colors.surfaceContainerHighest(),
  outline: colors.outline(),
  "outline-variant": colors.outlineVariant(),
  scrim: colors.scrim(),
};

function declarations(seed: string, isDark: boolean): string {
  const scheme = new SchemeTonalSpot(Hct.fromInt(argbFromHex(seed)), isDark, 0);
  return Object.entries(ROLES)
    .map(([name, color]) => `--md-sys-color-${name}:${hexFromArgb(color.getArgb(scheme))};`)
    .join("");
}

/** Light and dark Material color schemes for a seed color, as CSS. */
export function themeCss(seed: string): string {
  return (
    `:root{${declarations(seed, true)}}` +
    `:root[data-theme='light']{${declarations(seed, false)}}`
  );
}
