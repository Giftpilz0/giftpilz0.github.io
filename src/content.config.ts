import { defineCollection } from "astro:content";
import { z } from "astro/zod";
import { docsLoader, i18nLoader } from "@astrojs/starlight/loaders";
import { docsSchema, i18nSchema } from "@astrojs/starlight/schema";

const ansibleVariable = z.object({
  name: z.string(),
  type: z.string(),
  required: z.boolean().default(false),
  description: z.string().optional(),
  default: z.string().optional(),
  choices: z.array(z.string()).optional(),
  get options() {
    return z.array(ansibleVariable).optional();
  },
});

export type AnsibleVariable = z.infer<typeof ansibleVariable>;

const ansible = z.object({
  /** Set on generated role pages. */
  ansibleRole: z
    .object({ collection: z.string(), name: z.string(), variables: z.array(ansibleVariable) })
    .optional(),
  /** Set on generated collection overview pages. */
  ansibleCollection: z
    .object({
      name: z.string(),
      roles: z.array(
        z.object({
          name: z.string(),
          description: z.string().optional(),
          variables: z.number(),
        }),
      ),
    })
    .optional(),
});

export const collections = {
  docs: defineCollection({ loader: docsLoader(), schema: docsSchema({ extend: ansible }) }),
  i18n: defineCollection({ loader: i18nLoader(), schema: i18nSchema() }),
};
