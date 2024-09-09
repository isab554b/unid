% for testimonial in frontpage_content['testimonials_section']['testimonials']:
<div class="bg-unidLigthPink p-8 rounded-lg space-y-12">
  <div class="space-y-6">
    <div id="icon_medium" class="size-6 text-unidLightBlue">
      <!-- prettier-ignore -->
      % include(f'{frontpage_content["testimonials_section"]["testimonial_icon"]}')
    </div>
    <p class="text-unidDarkBlue italic">{{ testimonial["text"] }}</p>
  </div>
  <div class="inline-flex items-center gap-4">
    <div class="justify-center flex flex-col">
      <p id="content_box_header_text">
        {{ testimonial["author_name"] }}
      </p>
      <p class="text-unidDarkBlue text-sm">
        {{ testimonial["author_job_title"] }}
      </p>
    </div>
  </div>
</div>
% end
