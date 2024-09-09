<!-- prettier-ignore -->
% for subscription_key, subscription in services_and_prices_content['subscription_section']['subscriptions']['subscription_default'].items():
<div>
  <div class="flex justify-end"></div>
  <div class="rounded-lg border-2 bg-unidYellow border-unidBlue flex flex-col">
    <div class="flex flex-col lg:flex-row justify-between gap-6">
      <div class="text-unidDarkBlue space-y-1 p-6">
        <h3>{{ subscription["info"]["hours"] }}</h3>
      </div>
    </div>
    <div class="border-b border-unidLightBlue mx-6"></div>
    <div class="p-6 space-y-6">
      <div class="space-y-2">
        % for point in subscription['selling_points']:
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
            class="text-unidDarkBlue text-right text-2xl xl:text-3xl font-saira font-bold"
          >
            {{ subscription["info"]["price"] }}
          </p>
          <div class="flex flex-col text-xs text-unidDarkBlue">
            <p>ekskl.</p>
            <p>moms</p>
          </div>
        </div>
      </div>
      <div class="flex justify-center text-center">
        <p class="italic text-sm text-unidDarkBlue">
          Der er en bindingsperiode på 3 måneder. Vær opmærksom på, at de 30
          minutters sparring ikke kan overføres til den næste måned.
        </p>
      </div>
    </div>
  </div>
</div>
% end
