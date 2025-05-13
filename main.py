# main.py

from langchain.agents import Tool
from langchain.chat_models import ChatOpenAI
from crewai import Agent, Crew
from langgraph.graph import StateGraph
from tools.satellite import SatelliteDataRetriever
from tools.gps import NavicGPSProcessor
from tools.drone import DroneSimController
from tools.threat import SignalIntelParser
from tools.comms import MeshNetSim

llm = ChatOpenAI(temperature=0)

SatComAgent = Agent(role="Data Collector", goal="Collect and interpret satellite imagery in real-time",
    tools=[Tool(name="SatelliteData", func=SatelliteDataRetriever(), description="Fetches satellite data")], llm=llm)

GeoNavAgent = Agent(role="Navigation Specialist", goal="Convert NAVIC signals into usable 3D paths for drones",
    tools=[Tool(name="NavicGPS", func=NavicGPSProcessor(), description="Processes NAVIC GPS data")], llm=llm)

DroneCommandAgent = Agent(role="Tactical Drone Commander", goal="Deploy drones using swarm logic and live instructions",
    tools=[Tool(name="DroneController", func=DroneSimController(), description="Simulates drone control")], llm=llm)

ThreatDetectionAgent = Agent(role="Intel Analyst", goal="Analyze radar and signal data for real-time threat mapping",
    tools=[Tool(name="SignalParser", func=SignalIntelParser(), description="Analyzes threat signals")], llm=llm)

SecureComAgent = Agent(role="Comms Engineer", goal="Maintain secure battlefield communication mesh",
    tools=[Tool(name="CommsSimulator", func=MeshNetSim(), description="Simulates battlefield mesh")], llm=llm)

CombatCloudAgent = Agent(role="Chief Coordinator", goal="Ensure continuous decision loop, coordination and agent sync", llm=llm)

crew = Crew(
    agents=[SatComAgent, GeoNavAgent, DroneCommandAgent, ThreatDetectionAgent, SecureComAgent, CombatCloudAgent],
    objective="Simulate real-time autonomous defense loop using satellite, GPS, drone, threat, and communication AI agents",
    process="multi-agent",
    coordinator=CombatCloudAgent
)

workflow = StateGraph()
workflow.add_node("Satellite", SatComAgent)
workflow.add_node("GPS", GeoNavAgent)
workflow.add_node("Drone", DroneCommandAgent)
workflow.add_node("Threat", ThreatDetectionAgent)
workflow.add_node("Cloud", CombatCloudAgent)
workflow.add_node("Comms", SecureComAgent)

workflow.set_entry_point("Satellite")
workflow.add_edge("Satellite", "GPS")
workflow.add_edge("GPS", "Drone")
workflow.add_edge("Drone", "Threat")
workflow.add_edge("Threat", "Cloud")
workflow.add_edge("Cloud", "Drone")
workflow.add_edge("Cloud", "Comms")

graph = workflow.compile()
# Run using: crew.kickoff() or graph.invoke()
