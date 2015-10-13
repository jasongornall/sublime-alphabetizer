import sublime, sublime_plugin


# simple function to alphabetize selected sections
class AlphabetizeCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    sections = []
    regions = self.view.sel()
    for region in regions:
      # Get the selected text
      sections.append(self.view.substr(region))
      # Transform it via rot13

    sections.sort()

    index = 0
    for region in regions:
      self.view.replace(edit, region, sections[index])
      index += 1
