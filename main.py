import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class ValorantAgent:
    def __init__(self, name, age, category, country, abilities, description, image_path=None):
        self.name = name
        self.age = age
        self.category = category
        self.country = country
        self.abilities = abilities
        self.description = description
        self.image_path = image_path

    def get_info(self):
        info = f"--- Agent Information ---\n"
        info += f"Name       : {self.name}\n"
        info += f"Age        : {self.age}\n"
        info += f"Role       : {self.category}\n"
        info += f"Origin     : {self.country}\n"
        info += f"Abilities  : {', '.join(self.abilities)}\n"
        info += f"Description: {self.description}\n"
        return info

class ValorantDatabase:
    def __init__(self):
        self.agents = self._load_agents()

    def _load_agents(self):
        return {
            "Brimstone": ValorantAgent(
                "Brimstone", 45, "Controller", "Baltimore, USA",
                ["Incendiary", "Stim Beacon", "Sky Smoke", "Orbital Strike"],
                "Tactical commander providing precise smoke and fire support.",
                image_path="images/Brimstone.jpeg"
            ),
            "Phoenix": ValorantAgent(
                "Phoenix", 25, "Duelist", "London, UK",
                ["Hot Hands", "Curveball", "Blaze", "Run It Back"],
                "A self-sustaining duelist who uses fire to blind, heal, and control space.",
                image_path="images/Phoenix.jpeg"
            ),
            "Sage": ValorantAgent(
                "Sage", 27, "Sentinel", "Shanghai, China",
                ["Barrier Orb", "Slow Orb", "Healing Orb", "Resurrection"],
                "A healer who ensures safety and sustainability for her team.",
                image_path="images/Sage.jpeg"
            ),
            "Sova": ValorantAgent(
                "Sova", 30, "Initiator", "Severomorsk, Russia",
                ["Owl Drone", "Shock Bolt", "Recon Bolt", "Hunter's Fury"],
                "A scout who reveals and hunts down enemies with precision.",
                image_path="images/Sova.jpeg"
            ),
            "Viper": ValorantAgent(
                "Viper", 32, "Controller", "USA",
                ["Snake Bite", "Poison Cloud", "Toxic Screen", "Viper's Pit"],
                "A chemist who controls the battlefield using toxic gases and chemicals.",
                image_path="images/Viper.jpeg"
            ),
            "Cypher": ValorantAgent(
                "Cypher", 35, "Sentinel", "Morocco",
                ["Trapwire", "Cyber Cage", "Spycam", "Neural Theft"],
                "A surveillance expert who gathers intel and monitors enemy movement.",
                image_path="images/Cypher.jpeg"
            ),
            "Reyna": ValorantAgent(
                "Reyna", 25, "Duelist", "Mexico",
                ["Leer", "Devour", "Dismiss", "Empress"],
                "Feeds off the souls of her enemies, becoming stronger after each kill.",
                image_path="images/Reyna.jpeg"
            ),
            "Killjoy": ValorantAgent(
                "Killjoy", 22, "Sentinel", "Berlin, Germany",
                ["Nanoswarm", "Alarmbot", "Turret", "Lockdown"],
                "A tech genius who secures areas with her automated gadgets.",
                image_path="images/Killjoy.jpeg"
            ),
            "Breach": ValorantAgent(
                "Breach", 35, "Initiator", "Sweden",
                ["Aftershock", "Flashpoint", "Fault Line", "Rolling Thunder"],
                "An initiator who uses seismic blasts to open paths and disorient foes.",
                image_path="images/Breach.jpeg"
            ),
            "Omen": ValorantAgent(
                "Omen", "Unknown", "Controller", "Unknown",
                ["Shrouded Step", "Paranoia", "Dark Cover", "From the Shadows"],
                "A shadowy figure who strikes fear and confusion into enemies.",
                image_path="images/Omen.jpeg"
            ),
            "Jett": ValorantAgent(
                "Jett", 20, "Duelist", "Seoul, South Korea",
                ["Cloudburst", "Updraft", "Tailwind", "Blade Storm"],
                "A hyper-agile fighter who outmaneuvers enemies with incredible speed.",
                image_path="images/Jett.jpeg"
            ),
            "Raze": ValorantAgent(
                "Raze", 21, "Duelist", "Rio de Janeiro, Brazil",
                ["Boom Bot", "Blast Pack", "Paint Shells", "Showstopper"],
                "An explosive expert who thrives on chaos and heavy firepower.",
                image_path="images/Raze.jpeg"
            ),
            "Skye": ValorantAgent(
                "Skye", 28, "Initiator", "Australia",
                ["Regrowth", "Trailblazer", "Guiding Light", "Seekers"],
                "Leads her team with healing and scouting abilities using her nature powers.",
                image_path="images/Skye.jpeg"
            ),
            "Yoru": ValorantAgent(
                "Yoru", 25, "Duelist", "Tokyo, Japan",
                ["Fakeout", "Blindside", "Gatecrash", "Dimensional Drift"],
                "A duelist who manipulates space and reality to deceive enemies.",
                image_path="images/Yoru.jpeg"
            ),
            "Astra": ValorantAgent(
                "Astra", 25, "Controller", "Ghana",
                ["Gravity Well", "Nova Pulse", "Nebula", "Astral Form"],
                "Uses cosmic energy to control the battlefield from the stars.",
                image_path="images/Astra.jpeg"
            ),
            "KAY/O": ValorantAgent(
                "KAY/O", "Unknown", "Initiator", "Unknown (Robot)",
                ["FRAG/ment", "FLASH/drive", "ZERO/point", "NULL/cmd"],
                "A robotic initiator built to suppress enemy abilities and lead the charge.",
                image_path="images/KAYO.jpeg"
            ),
            "Chamber": ValorantAgent(
                "Chamber", 30, "Sentinel", "France",
                ["Trademark", "Headhunter", "Rendezvous", "Tour De Force"],
                "An elegant marksman who uses technology to control and dominate space.",
                image_path="images/Chamber.jpeg"
            ),
            "Neon": ValorantAgent(
                "Neon", 19, "Duelist", "Manila, Philippines",
                ["Fast Lane", "Relay Bolt", "High Gear", "Overdrive"],
                "Moves at lightning speed, overwhelming enemies with quick strikes.",
                image_path="images/Neon.jpeg"
            ),
            "Fade": ValorantAgent(
                "Fade", 30, "Initiator", "Turkey",
                ["Prowler", "Seize", "Haunt", "Nightfall"],
                "A bounty hunter who uses fear and shadows to expose and capture foes.",
                image_path="images/Fade.jpeg"
            ),
            "Harbor": ValorantAgent(
                "Harbor", 34, "Controller", "India",
                ["Cascade", "Cove", "High Tide", "Reckoning"],
                "Commands the power of water to shape the battlefield and protect allies.",
                image_path="images/Harbor.jpeg"
            ),
            "Gekko": ValorantAgent(
                "Gekko", 20, "Initiator", "Los Angeles, USA",
                ["Dizzy", "Wingman", "Mosh Pit", "Thrash"],
                "Leads a team of creature companions that disrupt and disable enemies.",
                image_path="images/Gekko.jpeg"
            ),
            "Deadlock": ValorantAgent(
                "Deadlock", 35, "Sentinel", "Norway",
                ["GravNet", "Sonic Sensor", "Barrier Mesh", "Annihilation"],
                "Deploys advanced nanowire tech to trap and neutralize enemies.",
                image_path="images/Deadlock.jpeg"
            ),
            "Iso": ValorantAgent(
                "Iso", 28, "Duelist", "China",
                ["Undercut", "Double Tap", "Contingency", "Kill Contract"],
                "A freelance fixer who isolates enemies in one-on-one duels.",
                image_path="images/Iso.jpeg"
            ),
            "Clove": ValorantAgent(
                "Clove", 27, "Controller", "Scotland",
                ["Ruse", "Meddle", "Pick-Me-Up", "Not Dead Yet"],
                "A mischievous controller who manipulates death energy to stay in the fight.",
                image_path="images/Clove.jpeg"
            ),
            "Vyse": ValorantAgent(
                "Vyse", 32, "Sentinel", "Unknown (Eastern Europe)",
                ["Erosion", "Barbwire", "Magnet Mine", "Crucible"],
                "A sentinel who uses metallic constructs to block, trap, and corrode enemies.",
                image_path="images/Vyse.jpeg"
            ),
            "Tejo": ValorantAgent(
                "Tejo", 26, "Initiator", "Brazil",
                ["Flashbang", "Sticky Trap", "Shockwave", "Overclock"],
                "A tactical initiator who excels at creating openings and controlling enemy movement.",
                image_path="images/Tejo.jpeg"
            ),
            "Veto": ValorantAgent(
                "Veto", 29, "Duelist", "USA",
                ["Pierce", "Decoy", "Rapid Fire", "Final Strike"],
                "A high-risk, high-reward duelist who thrives on aggressive plays and clutch scenarios.",
                image_path="images/Veto.jpeg"
            ),
            "Waylay": ValorantAgent(
                "Waylay", 31, "Controller", "UK",
                ["Smoke Veil", "Tripwire", "Trapfield", "Nightfall"],
                "A master manipulator of terrain and vision, creating chaos for enemies while protecting teammates.",
                image_path="images/Waylay.jpeg"
            ),
        }

    def get_agent(self, name):
        return self.agents.get(name, None)

#GUI
def run_gui():
    db = ValorantDatabase()

    root = tk.Tk()
    root.title("Valorant Agent Viewer")
    root.geometry("700x500")

    ttk.Label(root, text="Select an Agent:", font=("Arial", 12)).pack(pady=10)

    selected = tk.StringVar()
    combo = ttk.Combobox(root, textvariable=selected, values=list(db.agents.keys()), state="readonly")
    combo.pack(pady=5)

    # Image display label
    image_label = ttk.Label(root)
    image_label.pack(pady=10)

    # Text info area
    text_area = tk.Text(root, width=80, height=15, font=("Courier", 10), state="disabled")
    text_area.pack(pady=10)

    def show_info():
        name = selected.get()
        agent = db.get_agent(name)

        text_area.config(state="normal")
        text_area.delete("1.0", tk.END)

        if agent:
            text_area.insert(tk.END, agent.get_info())

            # Display Image
            if agent.image_path:
                try:
                    img = Image.open(agent.image_path)
                    img = img.resize((220, 220))
                    photo = ImageTk.PhotoImage(img)

                    image_label.config(image=photo)
                    image_label.image = photo  
                except Exception as e:
                    image_label.config(text="Image failed to load")
            else:
                image_label.config(image="", text="No Image")
        else:
            text_area.insert(tk.END, "Agent not found.")
            image_label.config(image="", text="")

        text_area.config(state="disabled")

    ttk.Button(root, text="Show Details", command=show_info).pack(pady=5)

    root.mainloop()
    
if __name__ == "__main__":
    run_gui()
