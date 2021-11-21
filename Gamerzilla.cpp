#include "Gamerzilla.hpp"

#include "Input.hpp"
#include "File.hpp"

#include <gamerzilla.h>
#include <string>

using namespace godot;

static size_t godotFileSize(const char *filename) {
	Ref<File> file;
	file.instance();

	file->open(filename, File::READ);
	size_t s = file->get_len();
	file->close();

	return s;
}

static void *godotFileOpen(const char *filename) {
	Ref<File> file;
	file.instance();

	file->open(filename, File::READ);
	file->reference();
	return file.ptr();
}

static size_t godotFileRead(void *fd, void *buf, size_t count) {
	int pos1 = ((File*)fd)->get_position();
	int maxpos = ((File*)fd)->get_len();
	if (pos1 + count > maxpos)
		count = maxpos - pos1;
	PoolByteArray c = ((File*)fd)->get_buffer(count);
	int pos2 = ((File*)fd)->get_position();
	for (int i = 0; i < pos2 - pos1; i++)
		((char *)buf)[i] = c[i];
	return pos2 - pos1;
}

static void godotFileClose(void *fd) {
	((File *)fd)->reference();
}

void GDGamerzilla::_register_methods() {
	godot::register_method("start", &GDGamerzilla::start);
	godot::register_method("getTrophy", &GDGamerzilla::getTrophy);
	godot::register_method("getTrophyStat", &GDGamerzilla::getTrophyStat);
	godot::register_method("setGameFromFile", &GDGamerzilla::setGameFromFile);
	godot::register_method("setTrophy", &GDGamerzilla::setTrophy);
	godot::register_method("setTrophyStat", &GDGamerzilla::setTrophyStat);
}

void GDGamerzilla::_init() {
	game_id = -1;
}

bool GDGamerzilla::start(bool server, godot::String savedir) {
	GamerzillaSetRead(&godotFileSize, &godotFileOpen, &godotFileRead, &godotFileClose);
	std::string cpp_save_dir = savedir.alloc_c_string();
	if ((cpp_save_dir.length() > 0) && (cpp_save_dir[cpp_save_dir.length() - 1] != '/'))
		cpp_save_dir += "/";
	return GamerzillaStart(server, cpp_save_dir.c_str());
}

bool GDGamerzilla::getTrophy(godot::String name) {
	bool val = false;
	GamerzillaGetTrophy(game_id, name.alloc_c_string(), &val);
	return val;
}

int GDGamerzilla::getTrophyStat(godot::String name) {
	int val = 0;
	GamerzillaGetTrophyStat(game_id, name.alloc_c_string(), &val);
	return val;
}

void GDGamerzilla::setGameFromFile(godot::String filename, godot::String datadir) {
	game_id = GamerzillaSetGameFromFile(filename.alloc_c_string(), datadir.alloc_c_string());
}

void GDGamerzilla::setTrophy(godot::String name) {
	GamerzillaSetTrophy(game_id, name.alloc_c_string());
}

void GDGamerzilla::setTrophyStat(godot::String name, int progress) {
	GamerzillaSetTrophyStat(game_id, name.alloc_c_string(), progress);
}
