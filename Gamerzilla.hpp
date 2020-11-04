#include <Godot.hpp>

#include <Reference.hpp>
#include <Sprite.hpp>

class GDGamerzilla : public godot::Reference {
	GODOT_CLASS(GDGamerzilla, godot::Reference)

	int game_id;

public:
	static void _register_methods();

	void _init();

	bool start(bool server, godot::String savedir);
	bool getTrophy(godot::String name);
	int getTrophyStat(godot::String name);
	void setGameFromFile(godot::String filename, godot::String datadir);
	void setTrophy(godot::String name);
	void setTrophyStat(godot::String name, int progress);
};
