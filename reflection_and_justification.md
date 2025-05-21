
# Reflection and Justification Document

## Design Decisions
- Modular architecture ensures separation of concerns.
- Trajectories modeled as (x, y, z, t) tuples.
- Conflicts detected based on spatial and temporal proximity.

## Spatial & Temporal Checks
- Drones compared at each time step.
- Conflicts detected if within 2 meters and 1 second.

## AI Integration
- (Optional): AI module can be integrated to predict optimal trajectories.

## Edge Cases
- Resolution is altitude-based, ensuring minimal deviation.
- Drones rechecked after conflict resolution.

## Scalability
- Easily extendable to hundreds of drones using spatial partitioning.
