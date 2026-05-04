-- {{< downloads >}}
-- Reads track, klassenstufe, unit_nr, slug from the document's front matter
-- and emits a four-link callout block (article + slides + worksheet PDF + exam PDF).

local function pad2(n)
  n = tonumber(n) or 0
  if n < 10 then return string.format("0%d", n) end
  return tostring(n)
end

return {
  ["downloads"] = function(args, kwargs, meta)
    local track = pandoc.utils.stringify(meta.track or "")
    local klasse = pandoc.utils.stringify(meta.klassenstufe or "")
    local unit_nr = pandoc.utils.stringify(meta.unit_nr or "")
    local slug = pandoc.utils.stringify(meta.slug or "")

    if track == "" or klasse == "" or unit_nr == "" or slug == "" then
      return pandoc.RawBlock("markdown",
        "::: {.callout-warning}\nDownloads shortcode: missing front-matter (track, klassenstufe, unit_nr, slug).\n:::")
    end

    local nn = pad2(unit_nr)
    local kk = pad2(klasse)

    local article = string.format("unit%s_%s.html", nn, slug)
    local slides = string.format("unit%s_slides.html", nn)
    local worksheet = string.format("/downloads/%s/kl%s/unit%s_%s_worksheet.pdf", track, kk, nn, slug)
    local exam = string.format("/downloads/%s/kl%s/unit%s_%s_exam.pdf", track, kk, nn, slug)

    local md = table.concat({
      "::: {.callout-tip icon=false title=\"Downloads\"}",
      string.format("- [Unit article](%s)", article),
      string.format("- [Slide deck](%s)", slides),
      string.format("- [Worksheet (PDF)](%s)", worksheet),
      string.format("- [Exam example (PDF)](%s)", exam),
      ":::",
      ""
    }, "\n")

    return pandoc.RawBlock("markdown", md)
  end
}
