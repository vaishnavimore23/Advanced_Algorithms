from pomegranate import *

# Rain is the root node
rain = Node(DiscreteDistribution({
    "none":0.7,
    "light":0.2,
    "heavy":0.1
}), name="rain")

# Maintainence node is conditioned on rain
maintainance = Node(ConditionalProbabilityTable([
    ["none", "yes",0.4],
    ["none", "no",0.6],
    ["light", "yes",0.2],
    ["light", "no",0.8],
    ["heavy", "yes",0.1],
    ["heavy", "no",0.9]
],[rain.distribution]), name ="maintainance")

# Bus node os conditional on rain and maintenance
bus = Node(ConditionalProbabilityTable([
    ["none","yes","on time",0.8],
    ["none","yes", "delayed", 0.2],
    ["none","no", "on time", 0.9],
    ["none","no", "delayed",0.1],
    ["light","yes","on time",0.6],
    ["light","yes", "delayed", 0.4],
    ["light","no", "on time", 0.7],
    ["light","no", "delayed",0.3],
    ["heavy","yes","on time",0.4],
    ["heavy","yes", "delayed", 0.6],
    ["heavy","no", "on time", 0.5],
    ["heavy","no", "delayed",0.5]
], [rain.distribution,maintainance.distribution]), name="bus")

# Class is conditional on bus
classs = Node(ConditionalProbabilityTable([
    ["on time", "attend",0.9],
    ["on time", "miss",0.1],
    ["delayed", "attend",0.6],
    ["delayed", "miss",0.4]
],[bus.distribution]), name="classs") 

# Create Bayesian Netword and add nodes
model = BayesianNetwork()
model.add_states(rain,maintainance,bus,classs)

# Add edges connecting the nodes
model.add_edge(rain,maintainance)
model.add_edge(rain,bus)
model.add_edge(maintainance,bus)
model.add_edge(bus,classs)

# Finanlize model
model.bake()