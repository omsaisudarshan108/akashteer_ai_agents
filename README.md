# AkashTeer AI Agent System (Simulated)

This project simulates a simplified version of the AkashTeer AI-coordinated battlefield system using:

- **LangChain** for agent definitions and tool integrations
- **LangGraph** for defining a reactive decision graph
- **CrewAI** for orchestrating AI agents as a team

## 🧠 Key Agents

1. **SatCom Agent** - Simulates satellite surveillance
2. **GeoNav Agent** - Processes GPS-like signals
3. **Drone Command Agent** - Controls drone swarm behaviors
4. **Threat Detection Agent** - Detects and analyzes threats
5. **SecureCom Agent** - Manages secure battlefield mesh communication
6. **CombatCloud Agent** - Orchestrates decision-making and coordination

## ⚙️ How to Run

1. Install dependencies:
```bash
pip install langchain crewai langgraph openai
```

2. Run the main file:
```bash
python main.py
```

## 🧭 Project Structure

- `main.py`: Entry point with all agent definitions and orchestration logic
- `tools/`: Contains mock tools simulating satellite, GPS, drones, etc.
- `README.md`: Project documentation

## 🚀 Future Extensions

- Integrate real EO datasets
- Use real NAVIC data (where accessible)
- Add simulation visualizations

---

This is a tech demo and not an actual defense application.
