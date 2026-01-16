import React, { useState } from 'react';
import { ArrowRight, GitBranch, Network } from 'lucide-react';

const BinaryTreeSpanning = () => {
  const [selectedTab, setSelectedTab] = useState('tree');

  // Data pohon biner dengan 7 simpul
  const binaryTree = {
    nodes: ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    edges: [
      ['A', 'B'], ['A', 'C'],
      ['B', 'D'], ['B', 'E'],
      ['C', 'F'], ['C', 'G']
    ],
    levels: {
      0: ['A'],
      1: ['B', 'C'],
      2: ['D', 'E', 'F', 'G']
    }
  };

  // Graf contoh untuk spanning tree
  const graph = {
    nodes: ['A', 'B', 'C', 'D', 'E'],
    edges: [
      { from: 'A', to: 'B', weight: 2 },
      { from: 'A', to: 'C', weight: 3 },
      { from: 'B', to: 'C', weight: 1 },
      { from: 'B', to: 'D', weight: 4 },
      { from: 'C', to: 'D', weight: 2 },
      { from: 'C', to: 'E', weight: 5 },
      { from: 'D', to: 'E', weight: 3 }
    ]
  };

  // Minimum Spanning Tree (MST) menggunakan algoritma Kruskal
  const mst = {
    edges: [
      { from: 'B', to: 'C', weight: 1 },
      { from: 'A', to: 'B', weight: 2 },
      { from: 'C', to: 'D', weight: 2 },
      { from: 'D', to: 'E', weight: 3 }
    ],
    totalWeight: 8
  };

  // Spanning Tree lainnya (bukan minimum)
  const spanningTree = {
    edges: [
      { from: 'A', to: 'B', weight: 2 },
      { from: 'A', to: 'C', weight: 3 },
      { from: 'B', to: 'D', weight: 4 },
      { from: 'D', to: 'E', weight: 3 }
    ],
    totalWeight: 12
  };

  const renderBinaryTree = () => (
    <div className="bg-white p-6 rounded-lg shadow">
      <h3 className="text-lg font-semibold mb-4 flex items-center gap-2">
        <GitBranch className="w-5 h-5" />
        Pohon Biner dengan 7 Simpul
      </h3>
      
      <div className="mb-6">
        <svg width="500" height="300" className="mx-auto">
          {/* Edges */}
          <line x1="250" y1="50" x2="150" y2="120" stroke="#6366f1" strokeWidth="2" />
          <line x1="250" y1="50" x2="350" y2="120" stroke="#6366f1" strokeWidth="2" />
          <line x1="150" y1="120" x2="100" y2="190" stroke="#6366f1" strokeWidth="2" />
          <line x1="150" y1="120" x2="200" y2="190" stroke="#6366f1" strokeWidth="2" />
          <line x1="350" y1="120" x2="300" y2="190" stroke="#6366f1" strokeWidth="2" />
          <line x1="350" y1="120" x2="400" y2="190" stroke="#6366f1" strokeWidth="2" />
          
          {/* Nodes */}
          <circle cx="250" cy="50" r="25" fill="#6366f1" />
          <text x="250" y="58" textAnchor="middle" fill="white" fontSize="18" fontWeight="bold">A</text>
          
          <circle cx="150" cy="120" r="25" fill="#8b5cf6" />
          <text x="150" y="128" textAnchor="middle" fill="white" fontSize="18" fontWeight="bold">B</text>
          
          <circle cx="350" cy="120" r="25" fill="#8b5cf6" />
          <text x="350" y="128" textAnchor="middle" fill="white" fontSize="18" fontWeight="bold">C</text>
          
          <circle cx="100" cy="190" r="25" fill="#a78bfa" />
          <text x="100" y="198" textAnchor="middle" fill="white" fontSize="18" fontWeight="bold">D</text>
          
          <circle cx="200" cy="190" r="25" fill="#a78bfa" />
          <text x="200" y="198" textAnchor="middle" fill="white" fontSize="18" fontWeight="bold">E</text>
          
          <circle cx="300" cy="190" r="25" fill="#a78bfa" />
          <text x="300" y="198" textAnchor="middle" fill="white" fontSize="18" fontWeight="bold">F</text>
          
          <circle cx="400" cy="190" r="25" fill="#a78bfa" />
          <text x="400" y="198" textAnchor="middle" fill="white" fontSize="18" fontWeight="bold">G</text>
        </svg>
      </div>

      <div className="bg-blue-50 p-4 rounded-lg">
        <h4 className="font-semibold mb-2">Karakteristik Pohon Biner:</h4>
        <ul className="space-y-1 text-sm">
          <li>• Jumlah simpul (nodes): 7</li>
          <li>• Jumlah sisi (edges): 6</li>
          <li>• Tinggi pohon (height): 2</li>
          <li>• Simpul akar (root): A</li>
          <li>• Simpul daun (leaves): D, E, F, G</li>
        </ul>
      </div>
    </div>
  );

  const renderGraph = () => (
    <div className="bg-white p-6 rounded-lg shadow">
      <h3 className="text-lg font-semibold mb-4 flex items-center gap-2">
        <Network className="w-5 h-5" />
        Graf dengan Bobot
      </h3>
      
      <div className="mb-6">
        <svg width="500" height="350" className="mx-auto">
          {/* Edges with weights */}
          <line x1="100" y1="100" x2="250" y2="80" stroke="#94a3b8" strokeWidth="2" />
          <text x="165" y="80" fill="#64748b" fontSize="14" fontWeight="bold">2</text>
          
          <line x1="100" y1="100" x2="180" y2="200" stroke="#94a3b8" strokeWidth="2" />
          <text x="130" y="155" fill="#64748b" fontSize="14" fontWeight="bold">3</text>
          
          <line x1="250" y1="80" x2="180" y2="200" stroke="#94a3b8" strokeWidth="2" />
          <text x="205" y="145" fill="#64748b" fontSize="14" fontWeight="bold">1</text>
          
          <line x1="250" y1="80" x2="400" y2="120" stroke="#94a3b8" strokeWidth="2" />
          <text x="325" y="90" fill="#64748b" fontSize="14" fontWeight="bold">4</text>
          
          <line x1="180" y1="200" x2="400" y2="120" stroke="#94a3b8" strokeWidth="2" />
          <text x="280" y="165" fill="#64748b" fontSize="14" fontWeight="bold">2</text>
          
          <line x1="180" y1="200" x2="350" y2="270" stroke="#94a3b8" strokeWidth="2" />
          <text x="255" y="245" fill="#64748b" fontSize="14" fontWeight="bold">5</text>
          
          <line x1="400" y1="120" x2="350" y2="270" stroke="#94a3b8" strokeWidth="2" />
          <text x="385" y="200" fill="#64748b" fontSize="14" fontWeight="bold">3</text>
          
          {/* Nodes */}
          <circle cx="100" cy="100" r="25" fill="#10b981" />
          <text x="100" y="108" textAnchor="middle" fill="white" fontSize="18" fontWeight="bold">A</text>
          
          <circle cx="250" cy="80" r="25" fill="#10b981" />
          <text x="250" y="88" textAnchor="middle" fill="white" fontSize="18" fontWeight="bold">B</text>
          
          <circle cx="180" cy="200" r="25" fill="#10b981" />
          <text x="180" y="208" textAnchor="middle" fill="white" fontSize="18" fontWeight="bold">C</text>
          
          <circle cx="400" cy="120" r="25" fill="#10b981" />
          <text x="400" y="128" textAnchor="middle" fill="white" fontSize="18" fontWeight="bold">D</text>
          
          <circle cx="350" cy="270" r="25" fill="#10b981" />
          <text x="350" y="278" textAnchor="middle" fill="white" fontSize="18" fontWeight="bold">E</text>
        </svg>
      </div>

      <div className="bg-green-50 p-4 rounded-lg">
        <h4 className="font-semibold mb-2">Daftar Sisi dan Bobotnya:</h4>
        <div className="grid grid-cols-2 gap-2 text-sm">
          {graph.edges.map((edge, idx) => (
            <div key={idx} className="flex items-center gap-2">
              <span className="font-mono">{edge.from}-{edge.to}: {edge.weight}</span>
            </div>
          ))}
        </div>
      </div>
    </div>
  );

  const renderSpanningTrees = () => (
    <div className="space-y-6">
      {/* Minimum Spanning Tree */}
      <div className="bg-white p-6 rounded-lg shadow">
        <h3 className="text-lg font-semibold mb-4 text-emerald-600">
          Minimum Spanning Tree (MST)
        </h3>
        
        <div className="mb-6">
          <svg width="500" height="350" className="mx-auto">
            {/* MST Edges - highlighted */}
            <line x1="250" y1="80" x2="180" y2="200" stroke="#10b981" strokeWidth="3" />
            <text x="205" y="145" fill="#059669" fontSize="16" fontWeight="bold">1</text>
            
            <line x1="100" y1="100" x2="250" y2="80" stroke="#10b981" strokeWidth="3" />
            <text x="165" y="80" fill="#059669" fontSize="16" fontWeight="bold">2</text>
            
            <line x1="180" y1="200" x2="400" y2="120" stroke="#10b981" strokeWidth="3" />
            <text x="280" y="165" fill="#059669" fontSize="16" fontWeight="bold">2</text>
            
            <line x1="400" y1="120" x2="350" y2="270" stroke="#10b981" strokeWidth="3" />
            <text x="385" y="200" fill="#059669" fontSize="16" fontWeight="bold">3</text>
            
            {/* Non-MST edges - faded */}
            <line x1="100" y1="100" x2="180" y2="200" stroke="#e5e7eb" strokeWidth="2" strokeDasharray="5,5" />
            <line x1="250" y1="80" x2="400" y2="120" stroke="#e5e7eb" strokeWidth="2" strokeDasharray="5,5" />
            <line x1="180" y1="200" x2="350" y2="270" stroke="#e5e7eb" strokeWidth="2" strokeDasharray="5,5" />
            
            {/* Nodes */}
            <circle cx="100" cy="100" r="25" fill="#10b981" />
            <text x="100" y="108" textAnchor="middle" fill="white" fontSize="18" fontWeight="bold">A</text>
            
            <circle cx="250" cy="80" r="25" fill="#10b981" />
            <text x="250" y="88" textAnchor="middle" fill="white" fontSize="18" fontWeight="bold">B</text>
            
            <circle cx="180" cy="200" r="25" fill="#10b981" />
            <text x="180" y="208" textAnchor="middle" fill="white" fontSize="18" fontWeight="bold">C</text>
            
            <circle cx="400" cy="120" r="25" fill="#10b981" />
            <text x="400" y="128" textAnchor="middle" fill="white" fontSize="18" fontWeight="bold">D</text>
            
            <circle cx="350" cy="270" r="25" fill="#10b981" />
            <text x="350" y="278" textAnchor="middle" fill="white" fontSize="18" fontWeight="bold">E</text>
          </svg>
        </div>

        <div className="bg-emerald-50 p-4 rounded-lg">
          <h4 className="font-semibold mb-2">Sisi-sisi MST:</h4>
          <div className="space-y-1 text-sm mb-3">
            {mst.edges.map((edge, idx) => (
              <div key={idx}>• {edge.from}-{edge.to}: bobot {edge.weight}</div>
            ))}
          </div>
          <div className="text-lg font-bold text-emerald-700">
            Total Bobot Minimum: {mst.totalWeight}
          </div>
        </div>
      </div>

      {/* Another Spanning Tree */}
      <div className="bg-white p-6 rounded-lg shadow">
        <h3 className="text-lg font-semibold mb-4 text-blue-600">
          Spanning Tree Lainnya (Bukan Minimum)
        </h3>
        
        <div className="mb-6">
          <svg width="500" height="350" className="mx-auto">
            {/* ST Edges - highlighted */}
            <line x1="100" y1="100" x2="250" y2="80" stroke="#3b82f6" strokeWidth="3" />
            <text x="165" y="80" fill="#2563eb" fontSize="16" fontWeight="bold">2</text>
            
            <line x1="100" y1="100" x2="180" y2="200" stroke="#3b82f6" strokeWidth="3" />
            <text x="130" y="155" fill="#2563eb" fontSize="16" fontWeight="bold">3</text>
            
            <line x1="250" y1="80" x2="400" y2="120" stroke="#3b82f6" strokeWidth="3" />
            <text x="325" y="90" fill="#2563eb" fontSize="16" fontWeight="bold">4</text>
            
            <line x1="400" y1="120" x2="350" y2="270" stroke="#3b82f6" strokeWidth="3" />
            <text x="385" y="200" fill="#2563eb" fontSize="16" fontWeight="bold">3</text>
            
            {/* Non-ST edges - faded */}
            <line x1="250" y1="80" x2="180" y2="200" stroke="#e5e7eb" strokeWidth="2" strokeDasharray="5,5" />
            <line x1="180" y1="200" x2="400" y2="120" stroke="#e5e7eb" strokeWidth="2" strokeDasharray="5,5" />
            <line x1="180" y1="200" x2="350" y2="270" stroke="#e5e7eb" strokeWidth="2" strokeDasharray="5,5" />
            
            {/* Nodes */}
            <circle cx="100" cy="100" r="25" fill="#3b82f6" />
            <text x="100" y="108" textAnchor="middle" fill="white" fontSize="18" fontWeight="bold">A</text>
            
            <circle cx="250" cy="80" r="25" fill="#3b82f6" />
            <text x="250" y="88" textAnchor="middle" fill="white" fontSize="18" fontWeight="bold">B</text>
            
            <circle cx="180" cy="200" r="25" fill="#3b82f6" />
            <text x="180" y="208" textAnchor="middle" fill="white" fontSize="18" fontWeight="bold">C</text>
            
            <circle cx="400" cy="120" r="25" fill="#3b82f6" />
            <text x="400" y="128" textAnchor="middle" fill="white" fontSize="18" fontWeight="bold">D</text>
            
            <circle cx="350" cy="270" r="25" fill="#3b82f6" />
            <text x="350" y="278" textAnchor="middle" fill="white" fontSize="18" fontWeight="bold">E</text>
          </svg>
        </div>

        <div className="bg-blue-50 p-4 rounded-lg">
          <h4 className="font-semibold mb-2">Sisi-sisi Spanning Tree:</h4>
          <div className="space-y-1 text-sm mb-3">
            {spanningTree.edges.map((edge, idx) => (
              <div key={idx}>• {edge.from}-{edge.to}: bobot {edge.weight}</div>
            ))}
          </div>
          <div className="text-lg font-bold text-blue-700">
            Total Bobot: {spanningTree.totalWeight}
          </div>
        </div>
      </div>

      {/* Comparison */}
      <div className="bg-amber-50 p-4 rounded-lg">
        <h4 className="font-semibold mb-2 flex items-center gap-2">
          <ArrowRight className="w-5 h-5" />
          Perbedaan Spanning Tree dan Minimum Spanning Tree:
        </h4>
        <ul className="space-y-2 text-sm">
          <li>• <strong>Spanning Tree:</strong> Pohon yang menghubungkan semua simpul tanpa membentuk siklus. Total bobot bisa bervariasi.</li>
          <li>• <strong>Minimum Spanning Tree:</strong> Spanning tree dengan total bobot sisi yang paling kecil.</li>
          <li>• Dalam contoh ini: MST memiliki bobot {mst.totalWeight}, sedangkan spanning tree lain memiliki bobot {spanningTree.totalWeight}</li>
          <li>• Selisih: {spanningTree.totalWeight - mst.totalWeight} (MST lebih efisien)</li>
        </ul>
      </div>
    </div>
  );

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 p-8">
      <div className="max-w-6xl mx-auto">
        <div className="bg-white rounded-lg shadow-lg p-6 mb-6">
          <h1 className="text-3xl font-bold text-gray-800 mb-2">
            Pohon Biner dan Spanning Tree
          </h1>
          <p className="text-gray-600">
            Visualisasi dan analisis struktur data pohon biner serta spanning tree
          </p>
        </div>

        {/* Tabs */}
        <div className="flex gap-2 mb-6">
          <button
            onClick={() => setSelectedTab('tree')}
            className={`px-6 py-3 rounded-lg font-medium transition-colors ${
              selectedTab === 'tree'
                ? 'bg-blue-600 text-white shadow-lg'
                : 'bg-white text-gray-700 hover:bg-gray-50'
            }`}
          >
            Pohon Biner
          </button>
          <button
            onClick={() => setSelectedTab('graph')}
            className={`px-6 py-3 rounded-lg font-medium transition-colors ${
              selectedTab === 'graph'
                ? 'bg-green-600 text-white shadow-lg'
                : 'bg-white text-gray-700 hover:bg-gray-50'
            }`}
          >
            Graf
          </button>
          <button
            onClick={() => setSelectedTab('spanning')}
            className={`px-6 py-3 rounded-lg font-medium transition-colors ${
              selectedTab === 'spanning'
                ? 'bg-purple-600 text-white shadow-lg'
                : 'bg-white text-gray-700 hover:bg-gray-50'
            }`}
          >
            Spanning Tree
          </button>
        </div>

        {/* Content */}
        {selectedTab === 'tree' && renderBinaryTree()}
        {selectedTab === 'graph' && renderGraph()}
        {selectedTab === 'spanning' && renderSpanningTrees()}
      </div>
    </div>
  );
};

export default BinaryTreeSpanning;
