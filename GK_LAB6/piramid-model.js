function createHeptagonPyramid(radius = 5, height = 7.5) {
  const baseVertexCount = 7;
  const angleStep = (2 * Math.PI) / baseVertexCount;
  const vertexPositions = [];
  const vertexNormals = [];
  const indices = [];

  // Generate base vertices
  for (let i = 0; i < baseVertexCount; i++) {
    const angle = i * angleStep;
    const x = radius * Math.cos(angle);
    const z = radius * Math.sin(angle);
    vertexPositions.push(x, 0, z);
    vertexNormals.push(0, -1, 0); // normals for the base
  }

  // Top vertex
  vertexPositions.push(0, height, 0);
  const topIndex = baseVertexCount;
  
  // Fake normals for top vertex sides (one per face)
  for (let i = 0; i < baseVertexCount; i++) {
    const nextIndex = (i + 1) % baseVertexCount;
    const x1 = vertexPositions[i * 3];
    const z1 = vertexPositions[i * 3 + 2];
    const x2 = vertexPositions[nextIndex * 3];
    const z2 = vertexPositions[nextIndex * 3 + 2];
    
    // approximate normal (not normalized for simplicity)
    const nx = (x1 + x2) / 2;
    const ny = height / 2;
    const nz = (z1 + z2) / 2;
    vertexNormals.push(nx, ny, nz);
  }

  // Indices for base (fan triangle from center)
  for (let i = 1; i < baseVertexCount - 1; i++) {
    indices.push(0, i, i + 1);
  }

  // Indices for sides
  for (let i = 0; i < baseVertexCount; i++) {
    const next = (i + 1) % baseVertexCount;
    indices.push(i, next, topIndex);
  }

  return {
    vertexPositions: new Float32Array(vertexPositions),
    vertexNormals: new Float32Array(vertexNormals),
    indices: new Uint16Array(indices),
  };
}

const piramidModel = createHeptagonPyramid();