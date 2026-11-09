<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{{title}} — My Life Is Worth Living</title>
<meta name="description" content="{{desc}}">
<!-- @include head -->
</head>
<body>
<!-- @page watch -->
<!-- @include icons -->
<!-- @include header -->

<main id="main">

<!-- ========== Story player (Figma: Story / Story player). On WordPress: the Story single template with a YouTube embed. ========== -->
<section class="mliwl-band mliwl-page-head" aria-labelledby="story-title">
  <div class="mliwl-inner">
    <nav class="mliwl-breadcrumb" aria-label="Breadcrumb"><ol><li><a href="index.html">Home</a></li><li><a href="watch.html">Stories</a></li><li><span aria-current="page">{{title}}</span></li></ol></nav>
    <div class="mliwl-player-row" data-character="{{slug}}">
      <div class="mliwl-player-main">
        <div class="mliwl-player">
          <img src="assets/img/story-{{slug}}.webp" width="576" height="432" alt="">
          <a class="mliwl-player-play" href="#" aria-label="Play episode 1 of {{title}}"><svg aria-hidden="true"><use href="#i-play"/></svg></a>
        </div>
        <div class="mliwl-story-info">
          <div class="mliwl-tags"><span class="mliwl-tag mliwl-tag-highlight" id="episode-tag">Episode 1 of {{count}}</span><span class="mliwl-tag">Ages 13+</span><span class="mliwl-tag">Subtitles: EN · ES</span></div>
          <h1 id="story-title" class="text-heading-h1">{{title}}</h1>
          <p class="text-body-large mliwl-muted-text">{{desc}} [Client copy: 2–3 sentences about the story — what happens and what viewers will learn.]</p>
          <p class="text-body-small mliwl-muted-text">{{episodes}} · [total min] · Animated short</p>
          <div class="mliwl-content-note mliwl-story-note"><p class="text-body-strong">Content note</p><p class="text-body-small">Includes: {{note}}. Watch with a trusted adult if you need to. Need to talk? Call or text 988.</p></div>
          <div class="mliwl-actions">
            <a class="mliwl-btn mliwl-btn-primary" href="#" download><svg aria-hidden="true"><use href="#i-download"/></svg>Download {{lesson}}</a>
            <a class="mliwl-btn mliwl-btn-outline" href="#" lang="es"><svg aria-hidden="true"><use href="#i-globe"/></svg>Ver en español</a>
          </div>
        </div>
      </div>
      <aside class="mliwl-episodes" aria-labelledby="episodes-title">
        <div><h2 id="episodes-title" class="text-heading-h4">Episodes</h2><p class="text-body-small mliwl-muted-text">{{episodes}} · [total min]</p></div>
        <ol class="mliwl-episode-list">
{{episode_rows}}
        </ol>
        <div class="mliwl-after-series"><p class="text-eyebrow mliwl-eyebrow">After the last episode</p><p class="text-body-small">Talk about it with the <a href="#teach">discussion guide</a>, or <a href="get-help.html">reach out</a> if it brought something up.</p></div>
      </aside>
    </div>
  </div>
</section>

<!-- ========== Teach this story ========== -->
<section id="teach" class="mliwl-band mliwl-bg-muted" aria-labelledby="teach-title">
  <div class="mliwl-inner">
    <div class="mliwl-section-header">
      <p class="text-eyebrow mliwl-eyebrow">For educators and parents</p>
      <h2 id="teach-title" class="text-heading-h2">Teach {{title}}</h2>
      <p class="text-body-large mliwl-muted-text">Free resources to use in class or at home. No sign-up needed.</p>
    </div>
    <ul class="mliwl-card-grid">
      <li class="mliwl-resource"><span class="mliwl-icon-badge mliwl-icon-badge-gold mliwl-icon-badge-sm" aria-hidden="true"><svg><use href="#i-book"/></svg></span><h3 class="text-heading-h4">{{lesson_title}}</h3><p class="text-body-small mliwl-muted-text">A 45-minute class plan with goals, activities and discussion prompts.</p><p class="text-caption mliwl-muted-text">PDF · [size] · Grades 7–12</p><a class="mliwl-btn mliwl-btn-outline mliwl-btn-sm" href="#" download><svg aria-hidden="true"><use href="#i-download"/></svg>Download<span class="screen-reader-text"> {{lesson}}</span></a></li>
      <li class="mliwl-resource"><span class="mliwl-icon-badge mliwl-icon-badge-gold mliwl-icon-badge-sm" aria-hidden="true"><svg><use href="#i-message"/></svg></span><h3 class="text-heading-h4">Discussion guide</h3><p class="text-body-small mliwl-muted-text">Questions to talk through after each episode, in a group or one-on-one.</p><p class="text-caption mliwl-muted-text">PDF · [size]</p><a class="mliwl-btn mliwl-btn-outline mliwl-btn-sm" href="#" download><svg aria-hidden="true"><use href="#i-download"/></svg>Download<span class="screen-reader-text"> discussion guide</span></a></li>
      <li class="mliwl-resource"><span class="mliwl-icon-badge mliwl-icon-badge-gold mliwl-icon-badge-sm" aria-hidden="true"><svg><use href="#i-book"/></svg></span><h3 class="text-heading-h4">Parent playbook</h3><p class="text-body-small mliwl-muted-text">How to start the conversation at home and what to say if your teen opens up.</p><p class="text-caption mliwl-muted-text">PDF · [size]</p><a class="mliwl-btn mliwl-btn-outline mliwl-btn-sm" href="#" download><svg aria-hidden="true"><use href="#i-download"/></svg>Download<span class="screen-reader-text"> parent playbook</span></a></li>
    </ul>
  </div>
</section>

<!-- @include get-help -->

<!-- ========== More stories ========== -->
<section class="mliwl-band" aria-labelledby="more-title">
  <div class="mliwl-inner">
    <div class="mliwl-stories-top">
      <div class="mliwl-section-header">
        <p class="text-eyebrow mliwl-eyebrow">Keep watching</p>
        <h2 id="more-title" class="text-heading-h2">More stories</h2>
      </div>
      <a class="mliwl-btn mliwl-btn-outline" href="watch.html">See all 8 stories<svg aria-hidden="true"><use href="#i-arrow"/></svg></a>
    </div>
    <ul class="mliwl-story-grid mliwl-story-grid-3 mliwl-story-grid-stack" id="story-grid" data-exclude="{{slug}}" data-limit="3"></ul>
  </div>
</section>

</main>

<!-- @include footer -->

<script src="assets/site.js"></script>
</body>
</html>
