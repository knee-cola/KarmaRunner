import sublime
import sublime_plugin

# useful links
# http://stackoverflow.com/questions/41768673/let-sublime-choose-among-two-similar-build-systems/41815033
# http://www.programcreek.com/python/example/52601/sublime.load_settings

class run_karmaCommand(sublime_plugin.WindowCommand):
	def run(self):
		# http://www.programcreek.com/python/example/52601/sublime.load_settings

		# this flag will ENABLE the keyboard shotcut which prevents Esc button
		# from hiding the "Build Result Panel"
		sublime.load_settings("Preferences.sublime-settings").set("karma_running", True)

		# getting the name of the build system - the one stated in the sublime-project file
		build_system_name = sublime.load_settings("KarmaRunner.sublime-settings").get("build_system_name")

		# run the build task defined in the sublime-project file
		self.window.run_command("build", args={"name": build_system_name})
		self.window.run_command("build", args={"name": build_system_name})


class kill_karmaCommand(sublime_plugin.WindowCommand):
	def run(self):
		# http://www.programcreek.com/python/example/52601/sublime.load_settings
		settings = sublime.load_settings("Preferences.sublime-settings")
		# this flag will DISABLE the keyboard shotcut which prevents Esc button
		# from hiding the "Build Result Panel"
		settings.set("karma_running", False)
		
		# ask SublimeANSI to kill build process
		self.window.run_command("ansi_color_build", args={"kill": True})
		# hide the output panel
		self.window.run_command("hide_panel", args={"cancel": True})