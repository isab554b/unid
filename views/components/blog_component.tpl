<!-- prettier-ignore -->
% for post_key, post in blog_content['posts']['post_default'].items():

  <div>
    <!-- prettier-ignore -->
    <a href="{{ post['info']['link'] }}">
      <div class="space-y-3"> 
      <img src="/assets/images/blog/{{ post['info']['image'] }}" 
      alt="{{ post['info']['image_alt'] }}"
      class="object-cover w-full h-56 bg-center rounded-lg" />
    
    
    <!-- prettier-ignore -->
    <h4 class="text-xl text-unidDarkBlue">{{ post["info"]["title"] }}</h2>
    <p class="text-base text-unidDarkBlue" >
      {{ post["info"]["description"] }}
    </p>
    <!-- prettier-ignore -->
    <p class="font-medium text-sm text-unidDarkBlue">{{ post["info"]["author"] }} • {{ post["info"]["date"] }}</p>
    </div>
    </a>
  </div>

% end
