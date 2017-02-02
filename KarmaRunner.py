import sublime
import sublime_plugin

# useful links
# http://stackoverflow.com/questions/41768673/let-sublime-choose-among-two-similar-build-systems/41815033
# http://www.programcreek.com/python/example/52601/sublime.load_settings

_KarmaIsRunning = False
_showKarmaForFileType = ""

class run_karmaCommand(sublime_plugin.WindowCommand):
	def run(self):
		global _KarmaIsRunning
		global _showKarmaForFileType

		# run karma only iof it's not currently running
		if _KarmaIsRunning==False:

			settings = sublime.load_settings("KarmaRunner.sublime-settings")
			
			_showKarmaForFileType = "." + settings.get("show_karma_for_file_type")
			# listen for settings change
			settings.add_on_change("show_karma_for_file_type", lambda: self.reload_settings(settings))

			# getting the name of the build system - the one stated in the sublime-project file
			build_system_name = settings.get("build_system_name")

			# run the build task defined in the sublime-project file
			self.window.run_command("build", args={"name": build_system_name})
			_KarmaIsRunning = True

	# event hander for settings change
	def reload_settings(self, settings):
		global _showKarmaForFileType
		_showKarmaForFileType = "." + settings.get("show_karma_for_file_type")

class kill_karmaCommand(sublime_plugin.WindowCommand):
	def run(self):
		global _KarmaIsRunning

		# do nothing of Karma is not running
		if _KarmaIsRunning:
			# ask SublimeANSI to kill build process
			self.window.run_command("ansi_color_build", args={"kill": True})
			# hide the output panel
			self.window.run_command("hide_panel", args={"cancel": True})
			_KarmaIsRunning = False

			# stop listening on settings change
			sublime.load_settings("KarmaRunner.sublime-settings").clear_on_change("show_karma_for_file_type")

# Every time a file is saved show the output window,
# so that the test results can be seen
class karmaRunner_OnPostSave(sublime_plugin.EventListener):
	def on_post_save(self, view):
		global _KarmaIsRunning
		global _showKarmaForFileType

		# show panel only if Karma is currently running
		if _KarmaIsRunning:
			print(_showKarmaForFileType)
			# show panel only if the file type is JavaScript
			if view.file_name()[-3:]==_showKarmaForFileType:
				view.window().run_command("show_panel", args={"panel": "output.exec"})