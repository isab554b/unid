<div class="flex flex-col gap-y-6 md:gap-y-8">
  <div class="w-full gap-10 grid items-center grid-cols-1 md:grid-cols-2">
    <div class="flex flex-col gap-y-6 md:gap-y-8">
      <div class="space-y-2">
        <!-- prettier-ignore -->
        <p id="decorative_header">{{ about_us_content["vision_section"]["decorative_header_text"] }}</p>
        <h2>
          {{ about_us_content["vision_section"]["header_text"] }}
        </h2>
      </div>
      <div class="space-y-6">
        <!-- prettier-ignore -->
        % for paragraph in about_us_content['vision_section']['paragraphs']:
        <div class="space-y-2">
          <p id="paragraph_title">{{ paragraph["title"] }}</p>
          <p id="paragraph_text">
            {{ paragraph["text"] }}
          </p>
        </div>
        % end
      </div>
    </div>
    <div class="flex justify-center">
      <!-- prettier-ignore -->
      <img
            class="h-auto"
            src="/assets/illustrations/{{ about_us_content['vision_section']['illustration'] }}"
            alt="{{ about_us_content['vision_section']['illustration_alt'] }}"
          />
    </div>
  </div>
</div>
