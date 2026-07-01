<script setup>
import { ref, onMounted } from 'vue';

import { api } from './services/api'
import AppHeader from './components/AppHeader.vue'

const platforms = ref([]);

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
        class="block p-6 rounded-2xl border-2 transition-all duration-300 hover:-translate-y-1 hover:shadow-xl bg-gray-800"
      >
        <div class="flex items-center justify-between mb-4">
          <h2 class="text-2xl font-bold">{{ platform.name }}</h2>
          
          <div class="flex items-center gap-2">
            <span class="text-sm text-gray-400 capitalize">{{ platform.status }}</span>
            <span 
              class="w-3.5 h-3.5 rounded-full" 
              :class="statusColorClass(platform.status)"
            ></span>
          </div>
        </div>
        
        <p class="text-gray-300 mb-6 line-clamp-2">{{ platform.description }}</p>
        
        <div class="text-xs text-gray-500 uppercase tracking-wide font-semibold">
          Versione {{ platform.version }}
        </div>
      </a>

    </main>
    
    <div v-if="platforms.length === 0" class="text-center text-gray-500 mt-12">
      <p>Nessuna piattaforma registrata al momento. In attesa di segnali nello spazio...</p>
    </div>
  
  </div>
</template>
