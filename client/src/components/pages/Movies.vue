<template>
    <div>
      Movie page
    </div>
</template>

<script>
import router from '../../router';

export default {
  name: "Movies",
  mounted() {
    this.checkLoggedIn();
  },
  methods: {
    checkLoggedIn() {
      router.push('/auth');
    }
  }
};
</script>
