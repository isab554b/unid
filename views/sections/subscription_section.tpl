<div
  class="width_standard padding_y_standard space_y_standard space-y-24 mx-auto"
>
  <div class="flex flex-col gap-y-6 md:gap-y-8">
    <div class="w-full gap-10 grid items-center grid-cols-1 md:grid-cols-2">
      <div class="flex flex-col gap-y-6 md:gap-y-8">
        <div class="space-y-2">
          <!-- prettier-ignore -->
          <p id="decorative_header">{{ services_and_prices_content["subscription_section"]["decorative_header_text"] }}</p>
          <!-- prettier-ignore -->
          <h2>
          {{services_and_prices_content["subscription_section"]["header_text"]}}
        </h2>
        </div>
        <div class="space-y-6">
          <p id="introduction_text">
            <!-- prettier-ignore -->
            {{ services_and_prices_content["subscription_section"]["introduction_text"] }}
          </p>
          <!-- prettier-ignore -->
          % for paragraph in services_and_prices_content['subscription_section']['paragraphs']:
          <div class="space-y-2">
            <p id="paragraph_text">
              {{ paragraph["text"] }}
            </p>
          </div>
          % end
        </div>
      </div>
      <div class="flex justify-center items-center">
        <!-- prettier-ignore -->
        % include('components/subscription_component')
      </div>
    </div>
    <div class="flex justify-center text-center gap-1.5">
      <p class="italic text-sm">
        Du skal være logget ind for at købe et abonnement. Har du ikke en
        bruger?
      </p>
      <a
        href="/signup"
        class="group transition duration-300 cursor-pointer text-sm hover:scale-105 font-bold ease-in-out"
      >
        Opret en bruger
        <span
          class="block max-w-0 group-hover:max-w-full transition-all duration-500 h-0.5 bg-unidPurple"
        ></span>
      </a>
    </div>
  </div>
</div>
