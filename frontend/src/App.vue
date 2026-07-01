<script setup>
import { ref, onMounted, onUnmounted } from 'vue';

import { api } from './services/api'
import AppHeader from './components/AppHeader.vue'

const platforms = ref([]);
let pollingInterval = null;

const fetchPlatforms = async () => {
  try {
    const data = await api.getRegisteredPlatforms();
    platforms.value = data;
  } catch (error) {
    console.error("Errore durante il recupero delle piattaforme:", error);
  }
};

const statusColorClass = (status) => {
  switch (status) {
    case 'online': return 'bg-green-500 shadow-[0_0_10px_rgba(34,197,94,0.8)]';
    case 'warning': return 'bg-orange-500 shadow-[0_0_10px_rgba(249,115,22,0.8)]';
    case 'offline': return 'bg-red-500 shadow-[0_0_10px_rgba(239,68,68,0.8)]';
    default: return 'bg-gray-500';
  }
};

onMounted(() => {
  fetchPlatforms();

  pollingInterval = setInterval(() => {
    fetchPlatforms();
  }, 60000);
});

onUnmounted(() => {
  if (pollingInterval) {
    clearInterval(pollingInterval);
  }
});
</script>

<template>
  <div class="min-h-screen bg-brand-background text-brand-textMain font-sans pb-24 selection:bg-brand-primary selection:text-white">    
    
    <AppHeader />

    <main class="px-4 py-2 gap-7 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 max-w-6xl mx-auto">
      
      <a
        v-for="platform in platforms"
        :key="platform.id"
        :href="platform.url"
        target="_blank"
        rel="noopener noreferrer"
        class="block relative bg-gray-800 rounded-2xl p-6 transition-all duration-300 hover:-translate-y-1 hover:shadow-2xl overflow-hidden shadow-lg border border-gray-700/50"
      >
        <div class="flex items-center justify-between mb-3">
          
          <div class="flex items-center gap-3">
            <img 
              v-if="platform.icon" 
              :src="platform.icon" 
              :alt="platform.name + ' icon'"
              class="w-8 h-8 object-contain rounded-md"
            />
            <h2 class="text-2xl font-bold tracking-tight">{{ platform.name }}</h2>
          </div>
          
          <div class="flex items-center gap-3 text-sm">
            <span class="text-gray-400 font-mono">v{{ platform.version }}</span>
            <span 
              class="w-4 h-4 rounded-full" 
              :class="statusColorClass(platform.status, 'dot')"
            ></span>
          </div>
        </div>
        
        <p class="text-gray-300 text-base line-clamp-2">{{ platform.description }}</p>
      </a>

    </main>
    
    <div v-if="platforms.length === 0" class="text-center text-gray-500 mt-12 px-6">
      <p class="text-lg">Waiting for signals from space...</p>
      <p class="text-sm mt-1">No platforms registered.</p>
    </div>
  
  </div>
</template>
