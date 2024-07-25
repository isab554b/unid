<div class="bg-unidPink">
  <div
    class="width_standard padding_y_standard space_y_standard space-y-24 mx-auto"
  >
    <div class="flex flex-col gap-y-6 md:gap-y-8">
      <div class="w-full gap-10 grid grid-cols-1 md:grid-cols-2">
        <div class="flex flex-col gap-y-6 md:gap-y-8">
          <div class="space-y-2">
            <!-- prettier-ignore -->
            <p id="decorative_header">{{services_and_prices_content["prices_section"]["decorative_header_text"]}}</p>
            <h2>
              {{ services_and_prices_content["prices_section"]["header_text"] }}
            </h2>
          </div>
          <div class="space-y-6">
            <div class="space-y-2">
              <!-- prettier-ignore -->
              <p id="paragraph_title">{{services_and_prices_content["prices_section"]["paragraph_title"]}}</p>
            </div>
          </div>
        </div>
        <div class="flex items-end">
          <!-- prettier-ignore -->
          <p id="paragraph_text">
              {{services_and_prices_content["prices_section"]["paragraph_text"]}}
            </p>
        </div>
      </div>
      <div
        class="grid md:grid-cols-2 xl:grid-cols-3 grid-cols-1 justify-center items-end gap-10"
      >
        <!-- prettier-ignore -->
        % include('components/pricing_default_component')
      </div>
      <div class="flex justify-center text-center">
        <p class="italic text-sm">
          Der kan forekomme yderligere omkostninger i forbindelse med køb af
          tema eller plugins. <br />
          Ved køb af en af de ovenstående pakker, har UNID Studio ret, til at
          promovere sig selv på det færdige website.
        </p>
      </div>
    </div>

    <div class="flex flex-col gap-y-6 md:gap-y-8">
      <div class="flex md:justify-center text-center">
        <div
          class="space-y-2 flex flex-col items-center mx-auto justify-center"
        >
          <h2>
            <!-- prettier-ignore -->
            {{services_and_prices_content["addon_section"]["header_text"]}}
          </h2>
        </div>
      </div>
      <div class="">
        <!-- prettier-ignore -->
        % include('components/addon_component')
      </div>
      <div class="flex justify-center text-center">
        <p class="italic text-sm">
          Ved køb af hjemmesidepakke får man -20% på alle tilkøb. Rabatten er
          fratrukket ovenstående priser.
        </p>
      </div>
    </div>
  </div>
</div>

<div class="bg-unidYellow">
  <div
    class="width_standard padding_y_standard space_y_standard space-y-24 mx-auto"
  >
    <div class="flex flex-col gap-y-6 md:gap-y-8">
      <div class="flex md:justify-end md:text-right">
        <div class="space-y-2 md:w-1/2">
          <p id="decorative_header">
            <!-- prettier-ignore -->
            {{services_and_prices_content["clipcard_section"]["decorative_header_text"]}}
          </p>
          <!-- prettier-ignore -->
          <h2>{{services_and_prices_content["clipcard_section"]["header_text"]}}</h2>
        </div>
      </div>
      <div
        class="grid md:grid-cols-2 xl:grid-cols-3 grid-cols-1 justify-center items-end gap-10"
      >
        <!-- prettier-ignore -->
        % include('components/clipcard_component')
      </div>
      <div class="flex justify-center text-center gap-1.5">
        <p class="italic text-sm">
          Du skal være logget ind for at købe et klippekort. Har du ikke en
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
</div>
