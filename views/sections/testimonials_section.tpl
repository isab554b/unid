<section class="bg-unidLightPurple">
  <div class="width_standard mx-auto padding_y_standard space_y_standard">
    <div class="flex justify-center">
      <div
        class="lg:w-2/3 flex justify-center flex-col text-center gap-y-4 md:gap-y-6"
      >
        <div
          class="space-y-2 flex flex-col items-center mx-auto justify-center"
        >
          <!-- prettier-ignore -->
          <p id="decorative_header" class="text-white">{{ frontpage_content["testimonials_section"]["decorative_header_text"] }}</p>
          <h2>
            {{ frontpage_content["testimonials_section"]["header_text"] }}
          </h2>
        </div>
        <p id="subheader">
          {{ frontpage_content["testimonials_section"]["subheader_text"] }}
        </p>
      </div>
    </div>
    <div class="grid grid-cols-1 gap-8 lg:grid-cols-2 md:gap-10 lg:gap-16">
      <!-- prettier-ignore -->
      % include('components/testimonial_component')
    </div>
    <div class="flex justify-center">
      <a href="https://dk.trustpilot.com/review/unidstudio.dk" target="_blank">
        <button
          class="text-white text-sm md:text-base w-full lg:w-fit font-bold bg-unidDarkBlue py-3.5 px-10 rounded-md drop-shadow-xl transition ease-in-out duration-300 hover:scale-105"
        >
          Se flere anmeldelser
        </button>
      </a>
    </div>
  </div>
</section>
