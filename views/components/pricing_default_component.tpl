<!-- prettier-ignore -->
% for price_key, price in services_and_prices_content['prices_section']['pricings']['pricing_default'].items():
<div>
  <div class="flex justify-end">
    <div
      class="w-2/3 lg:w-3/5 bg-unidLightPurple border-2 border-unidDarkBlue border-b-0 rounded-t-lg"
    >
      <div class="flex gap-2 p-3 text-unidBeige items-center justify-center">
        <div class="w-6 h-6 text-unidDarkBlue">
          % include(global_content['ui_icons']['discount'])
        </div>
        <p class="font-medium text-sm tracking-wider text-unidDarkBlue">
          Studiepris:
          <br />
          <span class="font-bold">{{ price["info"]["discount"] }}</span>
        </p>
      </div>
    </div>
  </div>
  <div
    class="rounded-l-lg rounded-br-lg border-2 bg-unidLigthPink border-unidDarkBlue flex flex-col"
  >
    <div class="flex flex-col lg:flex-row justify-between gap-6">
      <div class="text-unidDarkBlue space-y-1 p-6">
        <h3>{{ price["info"]["hours"] }}</h3>
        <p class="text-sm tracking-widest title-font font-medium">
          {{ price["info"]["title"] }}
        </p>
      </div>
    </div>
    <div class="border-b border-unidLightBlue mx-6"></div>
    <div class="p-6 space-y-6">
      <div class="space-y-2">
        % for point in price['selling_points']:
        <div class="flex items-center gap-2 text-unidDarkBlue">
          <div class="text-unidDarkBlue w-5 h-5">
            % include(global_content['ui_icons']['checkmark'])
          </div>
          <p>{{ point["text"] }}</p>
        </div>
        % end
      </div>
      <div class="flex items-center justify-between gap-4">
        <p class="text-unidDarkBlue text-base lg:text-lg">Pris</p>
        <div class="flex items-center gap-2">
          <p
            class="text-unidDarkBlue text-right text-2xl xl:text-2xl font-saira font-bold"
          >
            {{ price["info"]["price"] }}
          </p>
          <div class="flex flex-col text-xs text-unidDarkBlue">
            <p>ekskl.</p>
            <p>moms</p>
          </div>
        </div>
      </div>
      <div class="space-y-2">
        <a href="/contact"
          ><button type="button" id="third_button">Kontakt nu</button></a
        >
      </div>
    </div>
  </div>
</div>
% end
