import sublime, sublime_plugin


# simple function to alphabetize selected sections
class AlphabetizeCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    sections = []
    regions = self.view.sel()
    for region in regions:

      # Get the selected text
      sections.append(self.view.substr(region))

    # let the python sort handle it
    sections.sort(key=lambda y: y.lower())

    # replace them inline
    index = 0
    for region in regions:
      self.view.replace(edit, region, sections[index])
      index += 1
